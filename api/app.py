import os
import uuid
import json
import time
from datetime import datetime

import redis
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_caching import Cache
import psycopg2
from dotenv import load_dotenv

load_dotenv()

from src.pipelines.run import MainPipeline

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("FLASK_DEBUG", "false").lower() == "true"
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_HOST"] = os.getenv("REDIS_HOST", "localhost")
app.config["CACHE_REDIS_PORT"] = int(os.getenv("REDIS_PORT", "6379"))
app.config["CACHE_REDIS_DB"] = int(os.getenv("REDIS_DB", "0"))

cache = Cache(app=app)
cache.init_app(app)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"), 
    port=int(os.getenv("REDIS_PORT", "6379")), 
    db=int(os.getenv("REDIS_DB", "0"))
)

db_conn = psycopg2.connect(
    database=os.getenv("DATABASE_NAME"), 
    user=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"), 
    host=os.getenv("DB_HOST", "localhost"), 
    port=os.getenv("PORT")
)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

CORS(
    app,
    origins = ALLOWED_ORIGINS
)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "success": True
    })

@app.route("/api/scrape_locations", methods=["POST"])
def scrape_locations(): # Change the naming of these at some point
    """Handle scraping request from React frontend."""
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({
                "success": False,
                "error": "No JSON data received. Make sure Content-Type is application/json"
            }), 400

        if not data or "role" not in data or not data.get("role"):
            return jsonify({
                "success": False,
                "error": "Role is required"
            }), 400
        
        user_inputs = {
            "role": data.get("role"),
            "uk_locations": data.get("uk_location"),
            "date_posted": data.get("date_posted"),
            "off_site": data.get("hybrid_or_remote"),
            "employment_types": data.get("employment_types")
        }
        
        main_pipeline = MainPipeline()
        job_listings = main_pipeline.job_search(user_inputs)

        job_listings_dict = job_listings.model_dump(exclude_none=True)

        job_search_id = str(uuid.uuid4())
        redis_key = job_search_id
        timeout = os.getenv("CACHE_DEFAULT_TIMEOUT")
        redis_client.setex(redis_key, timeout, json.dumps(job_listings_dict))

        metadata = {
            "job_search_id": job_search_id,
            "parameters": user_inputs,
            "timestamp": datetime.now().isoformat(),
            "job_count": len(job_listings_dict)
        }
        metadata_key = f"search_metadata:{job_search_id}"
        redis_client.setex(metadata_key, timeout, json.dumps(metadata))

        redis_client.zadd("recent_searches", {job_search_id: time.time()})
        redis_client.expire("recent_searches", timeout)

        return jsonify({
            "success": True,
            "job_search_id": job_search_id,
            "counts": {
                "responses": len(job_listings_dict),
            },
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/api/recent-searches", methods=["GET"])
def recent_searches():
    try:
        # Last 5 most recent searches
        search_ids = redis_client.zrevrange("recent_searches", 0, 4)

        recent_searches_list = []
        for id in search_ids:
            metadata_key = f"search_metadata:{id.decode()}"
            metadata_str = redis_client.get(metadata_key)

            if metadata_str is not None:
                metadata_dict = json.loads(metadata_str.decode("utf-8"))
                recent_searches_list.append(metadata_dict)
        
        return jsonify(recent_searches_list)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/api/project-ideas", methods=["POST"])
def project_ideas():
    try:
        data = request.get_json()

        existing_projects_id = f"ux_info:{data['job_search_id']}"
        existing_projects = redis_client.get(existing_projects_id)

        if existing_projects:
            str_projects = existing_projects.decode("utf-8")
            dict_projects = json.loads(str_projects)

            return jsonify({
                "id": existing_projects_id,
                "data": dict_projects
            })

        job_listings = redis_client.get(data["job_search_id"])
        str_job_listings = job_listings.decode("utf-8")
        dict_job_listings = json.loads(str_job_listings)

        main_pipeline = MainPipeline()
        ux_info = main_pipeline.project_idea_generation(dict_job_listings)

        ux_info_dict = ux_info.model_dump(exclude_none=True)

        ux_info_id = f"ux_info:{data['job_search_id']}"
        redis_key = ux_info_id
        timeout = os.getenv("CACHE_DEFAULT_TIMEOUT")
        redis_client.setex(redis_key, timeout, json.dumps(ux_info_dict))
        
        return(jsonify({
            "id": ux_info_id,
            "data": ux_info_dict
        }))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/api/project-evidence", methods=["POST"])
def project_evidence():
    try:
        data = request.get_json()

        ux_info = redis_client.get(data["id"])
        str_ux_info = ux_info.decode("utf-8")
        dict_ux_info = json.loads(str_ux_info)

        main_pipeline = MainPipeline()
        parsed_evidence = main_pipeline.parse_evidence(dict_ux_info)
        parsed_evidence_dict = parsed_evidence.model_dump(exclude_none=True)

        return jsonify(parsed_evidence_dict)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/api/save", methods=["POST"])
def save():
    try:
        data = request.get_json()
        db_cur = db_conn.cursor()

        id = data["save_project"]
        ux_info = redis_client.get(id)
        str_ux_info = ux_info.decode("utf-8")
        dict_ux_info = json.loads(str_ux_info)

        main_pipeline = MainPipeline()

        parsed_evidence = main_pipeline.parse_evidence(dict_ux_info)
        print(parsed_evidence)
        parsed_evidence_dict = parsed_evidence.model_dump(exclude_none=True)

        main_pipeline.save_project_data(
            dict_ux_info,
            parsed_evidence_dict,
            db_conn,
            db_cur
        )

        db_cur.close()

        return jsonify({
            "success": True,
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Make this more efficient by not passing all of the data (not all of it is needed for this stage)
@app.route("/api/fetch-saved-projects")
def fetch_saved_projects():
    db_cur = db_conn.cursor()

    main_pipeline = MainPipeline()
    fetched_data = main_pipeline.fetch_saved_data(db_conn, db_cur)

    db_cur.close()

    return jsonify(fetched_data.model_dump(exclude_none=True))


@app.route("/api/fetch-saved-project/<int:id>", methods=["GET"])
def fetch_saved_project(id):
    db_cur = db_conn.cursor()

    main_pipeline = MainPipeline()
    requested_data = main_pipeline.fetch_requested_data(id, db_conn, db_cur)

    db_cur.close()

    return jsonify(requested_data)

@app.route("/api/fetch-saved-project-evidence/<int:id>")
def fetch_saved_project_evidence(id):
    db_cur = db_conn.cursor()

    main_pipeline = MainPipeline()
    evidence = main_pipeline.fetch_saved_evidence(id, db_conn, db_cur)

    db_cur.close()

    return jsonify(evidence)

@app.route("/api/delete-saved-project/<int:id>", methods=["DELETE"])
def delete_saved_project(id):
    try:
        db_cur = db_conn.cursor()
        db_cur.execute("DELETE FROM history WHERE id = %s", (id,))
        db_conn.commit()
        db_cur.close()

        return jsonify({"success": True})
    except Exception as e:
        db_conn.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true", 
        host=os.getenv("FLASK_HOST", "0.0.0.0"), 
        port= int(os.getenv("FLASK_PORT", "5001"))
    )