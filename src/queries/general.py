ADD_HISTORY = """
    INSERT INTO history (title, parameters, project_list, evidence)
    VALUES (%s, %s, %s, %s)
    RETURNING id
"""

RETRIEVE_DATA = "SELECT * FROM history"

RETRIEVE_REQUESTED_DATA = "SELECT * FROM history WHERE id = %s"

RETRIEVE_REQUESTED_EVIDENCE = "SELECT evidence FROM history WHERE id = %s"