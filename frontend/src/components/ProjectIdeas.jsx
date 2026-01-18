import { useEffect, useState, useRef } from "react";
import { useParams, useNavigate, useBlocker, Link } from "react-router-dom";
import { Home, X } from "lucide-react";
import styles from '../styles/components/ProjectIdeas.module.css';
import API_URL from "../config";

function ProjectIdeas() {
    const { jobSearchId } = useParams();
    const [uxInformation, setUxInformation] = useState(null);
    const [savedProjects, setSavedProjects] = useState(null);
    const [isSaved, setIsSaved] = useState(false);
    const [deleteConfirmation, setDeleteConfirmation] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const hasFetchedRef = useRef(null);

    const blocker = useBlocker(({nextLocation}) => (
        nextLocation.pathname === "/"
    ))

    useEffect(() => {
        if (hasFetchedRef.current === jobSearchId) {
            return;
        }

        const active = sessionStorage.getItem("activeJobSearchId")

        if (active !== jobSearchId) {
            navigate("/", { replace: true })
            return
        }

        hasFetchedRef.current = jobSearchId;

        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/project-ideas`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ job_search_id: jobSearchId }),
                });

                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.error || "Failed to generate project ideas");
                }

                setUxInformation(data);
                sessionStorage.setItem("uxInfoId", data.id);
            } catch (err) {
                console.error('Error fetching project ideas:', err);
                setError(err);
                hasFetchedRef.current = null;
            }
        })();
        
    }, [jobSearchId, navigate]);

    useEffect(() => {
        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/fetch-saved-projects`);
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch saved projects");
                }

                setSavedProjects(data);
            } catch (err) {
                console.error('Error fetching saved projects:', err);
                // Non-critical: just set empty array
                setSavedProjects([]);
            }
        })();
    }, []);

    // Throw error during render to trigger ErrorBoundary
    if (error) {
        throw error;
    }

    if (!uxInformation) {
        return <div className="loading">Generating project ideas...</div>;
    }

    const projectList = uxInformation.data.project_list.projects
    const uxInfoId = uxInformation.id

    const handleSubmit = async (title) => {
        navigate(`/project-evidence/${uxInfoId}?project=${encodeURIComponent(title)}`);
    }

    const handleSave = async () => {
        try {
            const response = await fetch(`${API_URL}/api/save`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ save_project : uxInfoId })
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Failed to save project");
            }

            const fetchResponse = await fetch(`${API_URL}/api/fetch-saved-projects`);
            const fetchData = await fetchResponse.json();
            
            if (!fetchResponse.ok) {
                throw new Error(fetchData.error || "Failed to refresh saved projects");
            }

            setSavedProjects(fetchData);
            setIsSaved(true);
        } catch (err) {
            console.error('Error saving project:', err);
            setError(err);
        }
    }

    const handleDelete = async (e, projectId) => {
        e.preventDefault();
        e.stopPropagation();

        setDeleteConfirmation(projectId);
    }
    
    const confirmDelete = async (projectId) => {
        try {
            const response = await fetch(`${API_URL}/api/delete-saved-project/${projectId}`, {
                method: "DELETE",
            });
        
            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.error || "Failed to delete project");
            }
        
            setSavedProjects(prev => prev.filter(p => p.id !== projectId));
            setDeleteConfirmation(null);
        } catch (err) {
            console.error('Error deleting project:', err);
            setError(err);
        }
    }

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1 className={styles.title}>Project Ideas</h1>
                <div className={styles.actions}>
                    <button className={styles.saveBtn} onClick={handleSave} disabled={isSaved}>
                        Save Results
                    </button>
                </div>
            </header>

            <div className={styles.projectGrid}>
                {projectList.map((project, idx) => (
                    <article key={idx} className={styles.projectCard}>
                        <div className={styles.projectHeader}>
                            <h2 className={styles.projectTitle}>{project.title}</h2>
                            <span className={styles.projectNumber}>#{idx + 1}</span>
                        </div>

                        <div className={styles.section}>
                            <h3 className={styles.sectionTitle}>Problem Statement</h3>
                            <p className={styles.problemStatement}>{project.problem_statement}</p>
                        </div>

                        <div className={styles.section}>
                            <h3 className={styles.sectionTitle}>Core Features</h3>
                            <ul className={styles.featureList}>
                                {project.core_features.map((feature, i) => (
                                    <li key={i} className={styles.featureItem}>{feature}</li>
                                ))}
                            </ul>
                        </div>

                        <div className={styles.section}>
                            <h3 className={styles.sectionTitle}>Tech Stack</h3>
                            <ul className={styles.tagList}>
                                {project.recommended_tech_stack.map((tech, i) => (
                                    <li key={i} className={`${styles.tag} ${styles.techTag}`}>{tech}</li>
                                ))}
                            </ul>
                        </div>

                        <div className={styles.section}>
                            <h3 className={styles.sectionTitle}>Achieved Qualifications</h3>
                            <ul className={styles.tagList}>
                                {project.achieved_qualifications.map((qual, i) => (
                                    <li key={i} className={styles.tag}>{qual}</li>
                                ))}
                            </ul>
                        </div>

                        <div className={styles.section}>
                            <h3 className={styles.sectionTitle}>Target Users</h3>
                            <ul className={styles.tagList}>
                                {project.target_users.map((user, i) => (
                                    <li key={i} className={styles.tag}>{user}</li>
                                ))}
                            </ul>
                        </div>

                        <button 
                            className={styles.evidenceBtn} 
                            onClick={() => handleSubmit(project.title)}
                        >
                            View Market Evidence →
                        </button>
                    </article>
                ))}
            </div>

            {blocker.state === "blocked" && (
                <div className={styles.modal}>
                    <div className={styles.modalContent}>
                        <p className={styles.modalText}>
                            Are you sure you want to leave? You'll need to re-submit the form.
                        </p>
                        <div className={styles.modalActions}>
                            <button 
                                className={`${styles.modalBtn} ${styles.modalBtnSecondary}`}
                                onClick={() => blocker.reset()}
                            >
                                Stay
                            </button>
                            <button 
                                className={`${styles.modalBtn} ${styles.modalBtnPrimary}`}
                                onClick={() => blocker.proceed()}
                            >
                                Leave
                            </button>
                        </div>
                    </div>
                </div>
            )}

            <div className={styles.sideBar}>
                <button
                    className={styles.homeBtn}
                    onClick={() => navigate("/")}
                    aria-label="Home"
                >
                    <Home className={styles.homeIcon} />
                </button>

                {savedProjects && savedProjects.length > 0 && (
                    <aside className={styles.sidebar}>
                        <h3 className={styles.sidebarTitle}>Saved Results</h3>
                        <div className={styles.savedList}>
                            {savedProjects.map((projectLink) => (
                                <div key={projectLink.id} className={styles.savedItemWrapper}>
                                    <Link 
                                        to={`/saved-project/${projectLink.id}`}
                                        className={styles.savedItem}
                                    >
                                        {projectLink.title}
                                    </Link>
                                    <button
                                        className={styles.deleteBtn}
                                        onClick={(e) => handleDelete(e, projectLink.id)}
                                        aria-label="Delete saved project"
                                    >
                                        <X size={14} />
                                    </button>
                                </div>
                            ))}
                        </div>
                    </aside>
                )}
            </div>

            {deleteConfirmation && (
                <div className={styles.modal}>
                    <div className={styles.modalContent}>
                        <p className={styles.modalText}>
                            Are you sure you want to delete? This is a permanent change.
                        </p>
                        <div className={styles.modalActions}>
                            <button 
                                className={`${styles.modalBtn} ${styles.modalBtnSecondary}`}
                                onClick={() => setDeleteConfirmation(null)}
                            >
                                Undo
                            </button>
                            <button 
                                className={`${styles.modalBtn} ${styles.modalBtnPrimary}`}
                                onClick={() => confirmDelete(deleteConfirmation)}
                            >
                                Delete
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )

}

export default ProjectIdeas;
