import { useEffect, useState } from "react";
import { useParams, useLocation, useNavigate } from "react-router-dom";
import styles from '../styles/components/ProjectEvidence.module.css';
import API_URL from "../config";

function ProjectEvidence() {
    const { uxInfoId } = useParams();
    const { search } = useLocation();
    const [uxInformation, setUxInformation] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const projectTitle = search ? new URLSearchParams(search).get("project") : null;

    const jobSearchId = sessionStorage.getItem("activeJobSearchId");

    useEffect(() => {
        const active = sessionStorage.getItem("uxInfoId");

        if (active !== uxInfoId) {
            navigate(`/project-ideas/${jobSearchId}`);
            return;
        }

        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/project-evidence`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ id: uxInfoId }),
                });

                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch project evidence");
                }

                setUxInformation(data);
            } catch (err) {
                console.error('Error fetching project evidence:', err);
                setError(err);
            }
        })();
    }, [uxInfoId, jobSearchId, navigate]);

    // Throw error during render to trigger ErrorBoundary
    if (error) {
        throw error;
    }

    if (!uxInformation) {
        return <div className="loading">Loading evidence...</div>;
    }

    if (!projectTitle) {
        return (
            <div className={styles.container}>
                <div className={styles.empty}>No project specified</div>
            </div>
        );
    }

    const groupedByProject = uxInformation.reduce((acc, match) => {
        if (!acc[match.project_title]) {
            acc[match.project_title] = [];
        }
        acc[match.project_title].push(match);
        return acc;
    }, {});

    const matches = groupedByProject[projectTitle] || [];

    if (matches.length === 0) {
        return (
            <div className={styles.container}>
                <button 
                    className={styles.backBtn} 
                    onClick={() => navigate(`/project-ideas/${jobSearchId}`)}
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
                onClick={() => navigate(`/project-ideas/${jobSearchId}`)}
            >
                ← Back to Projects
            </button>

            <header className={styles.header}>
                <h1 className={styles.title}>Market Evidence</h1>
                <p className={styles.subtitle}>Real job listings that validate: {projectTitle}</p>
            </header>

            <div className={styles.evidenceList}>
                {matches.map((match, idx) => (
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

export default ProjectEvidence;
