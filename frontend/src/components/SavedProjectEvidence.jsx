import { useEffect, useState } from "react";
import { useParams, useLocation, useNavigate } from "react-router-dom";
import styles from '../styles/components/ProjectEvidence.module.css';
import API_URL from "../config";

function SavedProjectEvidence() {
    const { requestedDataId } = useParams();
    const { search } = useLocation();
    const [evidence, setEvidence] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const projectTitle = search ? new URLSearchParams(search).get("project") : null;

    useEffect(() => {
        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/fetch-saved-project-evidence/${requestedDataId}`);
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch saved project evidence");
                }
                
                setEvidence(data);
            } catch (err) {
                console.error('Error fetching saved project evidence:', err);
                setError(err);
            }
        })();
    }, [requestedDataId]);

    if (error) {
        throw error;
    }

    if (!evidence) {
        return <div className="loading">Retrieving evidence...</div>;
    }

    if (!projectTitle) {
        return (
            <div className={styles.container}>
                <div className={styles.empty}>No project specified</div>
            </div>
        );
    }

    const groupedByProject = evidence.filter(match => match.project_title === projectTitle);

    if (groupedByProject.length === 0) {
        return (
            <div className={styles.container}>
                <button 
                    className={styles.backBtn} 
                    onClick={() => navigate(`/saved-project/${requestedDataId}`)}
                >
                    ← Back to Projects
                </button>

                <header className={styles.header}>
                    <h1 className={styles.title}>Market Evidence</h1>
                    <p className={styles.subtitle}>Real job listings that validate: {projectTitle}</p>
                </header>

                <div className={styles.empty}>No evidence found for this project</div>
            </div>
        );
    }

    return (
        <div className={styles.container}>
            <button 
                className={styles.backBtn} 
                onClick={() => navigate(`/saved-project/${requestedDataId}`)}
            >
                ← Back to Projects
            </button>

            <header className={styles.header}>
                <h1 className={styles.title}>Market Evidence</h1>
                <p className={styles.subtitle}>Real job listings that validate: {projectTitle}</p>
            </header>

            <div className={styles.evidenceList}>
                {groupedByProject.map((match, idx) => (
                    <div key={idx} className={styles.evidenceCard}>
                        <div className={styles.matchHeader}>
                            <div className={styles.companyInfo}>
                                <div className={styles.jobTitle}>{match.job_title}</div>
                                <div className={styles.companyName}>{match.company_name}</div>
                            </div>
                        </div>

                        <div className={styles.matchSection}>
                            <div className={styles.matchLabel}>Your Project Achievement</div>
                            <div className={`${styles.matchText} ${styles.achievement}`}>
                                {match.project_achievement}
                            </div>
                        </div>

                        <div className={styles.matchSection}>
                            <div className={styles.matchLabel}>Job Requirement</div>
                            <div className={`${styles.matchText} ${styles.qualification}`}>
                                {match.qualification}
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SavedProjectEvidence;
