import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import styles from '../styles/components/ProjectIdeas.module.css';
import API_URL from "../config";

function SavedProject() {
    const { id } = useParams();
    const [requestedData, setRequestedData] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/fetch-saved-project/${id}`);
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch saved project");
                }
                
                setRequestedData(data);
            } catch (err) {
                console.error('Error fetching saved project:', err);
                setError(err);
            }
        })();
    }, [id]);

    // Throw error during render to trigger ErrorBoundary
    if (error) {
        throw error;
    }

    if (!requestedData) {
        return <div className="loading">Loading saved project...</div>;
    }

    const projectList = requestedData.project_list.projects;
    const requestedDataId = requestedData.id;
    const parameters = requestedData.parameters

    const handleSubmit = async (title) => {
        navigate(`/saved-project-evidence/${requestedDataId}?project=${encodeURIComponent(title)}`);
    };

    const jobSearchId = sessionStorage.getItem("activeJobSearchId");

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1 className={styles.title}>Saved Project Ideas</h1>
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

            <div className={styles.sideBar}>
                <button
                    className={styles.backBtn}
                    onClick={() => navigate(`/project-ideas/${jobSearchId}`)}
                >
                    ← All Projects
                </button>

                <aside className={styles.sidebar}>
                    <h3 className={styles.sidebarTitle}>Project Parameters</h3>

                    {parameters && (
                        <div className={styles.parametersList}>
                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Role</h4>
                                <span className={styles.paramValue}>{parameters.role}</span>
                            </div>

                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Country</h4>
                                <span className={styles.tag}>
                                    {parameters.country?.toUpperCase()}
                                </span>
                            </div>

                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Locations</h4>
                                <ul className={styles.tagList}>
                                    {Array.isArray(parameters.locations) 
                                        ? parameters.locations.map((loc, i) => (
                                            <li key={i} className={styles.tag}>{loc}</li>
                                        ))
                                        : <li className={styles.tag}>{parameters.locations || "All"}</li>
                                    }
                                </ul>
                            </div>

                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Posted</h4>
                                <span className={styles.tag}>{parameters.date_posted || "All Time"}</span>
                            </div>

                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Employment</h4>
                                <ul className={styles.tagList}>
                                    {Array.isArray(parameters.employment_types) 
                                        ? parameters.employment_types.map((type, i) => (
                                            <li key={i} className={styles.tag}>{type}</li>
                                        ))
                                        : <li className={styles.tag}>{parameters.employment_types || "All Types"}</li>
                                    }
                                </ul>
                            </div>

                            <div className={styles.paramSection}>
                                <h4 className={styles.paramSectionTitle}>Remote/Hybrid</h4>
                                <span className={styles.tag}>
                                    {parameters.off_site ? "True" : "False"}
                                </span>
                            </div>
                        </div>
                    )}
                </aside>
            </div>
        </div>
    );
}

export default SavedProject;
