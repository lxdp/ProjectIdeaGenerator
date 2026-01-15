import React, { useState, useEffect } from "react";
import Select from "react-select";
import { useNavigate, Link } from "react-router-dom";
import styles from '../styles/components/InitialForm.module.css';
import API_URL from "../config";

// Custom styles for react-select to match theme
const selectStyles = {
    control: (base, state) => ({
        ...base,
        background: 'var(--bg-card)',
        borderColor: state.isFocused ? 'var(--accent-primary)' : 'var(--border-color)',
        boxShadow: state.isFocused ? '0 0 0 3px var(--accent-glow)' : 'none',
        '&:hover': { borderColor: 'var(--accent-primary)' },
        padding: '4px',
        borderRadius: 'var(--radius-md)',
    }),
    menu: (base) => ({
        ...base,
        background: 'var(--bg-card)',
        border: '1px solid var(--border-color)',
        borderRadius: 'var(--radius-md)',
    }),
    option: (base, state) => ({
        ...base,
        background: state.isFocused ? 'var(--bg-card-hover)' : 'transparent',
        color: 'var(--text-primary)',
        '&:active': { background: 'var(--accent-glow)' },
    }),
    multiValue: (base) => ({
        ...base,
        background: 'var(--accent-glow)',
        borderRadius: 'var(--radius-sm)',
    }),
    multiValueLabel: (base) => ({
        ...base,
        color: 'var(--accent-primary)',
        fontWeight: 500,
    }),
    multiValueRemove: (base) => ({
        ...base,
        color: 'var(--accent-primary)',
        '&:hover': { background: 'var(--accent-primary)', color: 'var(--bg-primary)' },
    }),
    input: (base) => ({
        ...base,
        color: 'var(--text-primary)',
    }),
    placeholder: (base) => ({
        ...base,
        color: 'var(--text-muted)',
    }),
    singleValue: (base) => ({
        ...base,
        color: 'var(--text-primary)',
    }),
};

function InitForm() {

    const [error, setError] = useState(null);

    const MAX_LOCATIONS = 3;
    const MAX_EMP_TYPES = 2;

    const [formData, setFormData] = useState({
        "role": "",
        "uk_location": [],
        "date_posted": "",
        "hybrid_or_remote": false,
        "employment_types": []
    })

    const jobOptions = [
        {"label": "Full Time", "value": "full_time"},
        {"label": "Part Time", "value": "part_time"},
        {"label": "Internship", "value": "internship"},
        {"label": "Contract", "value": "contract"},
        {"label": "Temporary", "value": "temporary"},
        {"label": "Free Lance", "value": "free_lance"}
    ]

    const datePostedOptions = [
        {"label": "All time", "value": ""},
        {"label": "Today", "value": "86400"},
        {"label": "Last 3 days", "value": "259200"},
        {"label": "Last week", "value": "604800"},
        {"label": "Last month", "value": "2592000"}
    ]

    const [ukCities, setUkCities] = useState([]);

    useEffect(() => {
        (async () => {
            try {
                const response = await fetch('/ukCities.json');
                if (!response.ok) {
                    throw new Error(`Failed to load cities: ${response.status}`);
                }
                const data = await response.json();
                setUkCities(data);
            } catch (err) {
                console.error('Error fetching cities:', err);
                setError(err);
            }
        })();
    }, []);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target
        setFormData(prev => ({
            ...prev,
            [name]: type === "checkbox" ? checked : value
        }))
    }

    const handleMultiSelectChange = (selectedOptions, fieldName, max_length) => {
        const values = selectedOptions ? selectedOptions.map(option => option.value) : []

        if (values.length > max_length) return;

        setFormData(prev => ({
            ...prev,
            [fieldName]: values
        }))
    }

    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault()
        
        if (!e.target.checkValidity()) {
            e.target.reportValidity()
            return
        }

        try {
            const response = await fetch(`${API_URL}/api/scrape_locations`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'Failed to generate project ideas');
            } 

            const jobSearchId = data.job_search_id;
            sessionStorage.setItem("activeJobSearchId", jobSearchId)
            navigate(`/project-ideas/${jobSearchId}`);
        } catch (err) {
            console.error('Error sending data:', err)
            setError(err);
        }
    }

    useEffect(() => {
        sessionStorage.removeItem("activeJobSearchId")
    }, []);

    const [recentSearches, setRecentSearches] = useState([]);

    useEffect(() => {
        (async () => {
            try {
                const response = await fetch(`${API_URL}/api/recent-searches`);
                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.error || 'Failed to fetch recent searches');
                }

                setRecentSearches(data);
            } catch (err) {
                console.error('Error fetching recent searches:', err);
                // Don't set error for recent searches - it's non-critical
                setRecentSearches([]);
            }
        })();
    }, [])

    // Throw error during render to trigger ErrorBoundary
    if (error) {
        throw error;
    }

    sessionStorage.removeItem("uxInfoId")

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1 className={styles.logo}>ProjectForge</h1>
                <p className={styles.tagline}>Generate portfolio projects from real job market demand</p>
            </header>

            <form className={styles.form} onSubmit={handleSubmit}>
                <div className={styles.formGroup}>
                    <label className={styles.label} htmlFor="role">Job Role</label>
                    <input
                        className={styles.input}
                        name="role"
                        id="role"
                        type="text"
                        value={formData.role}
                        placeholder="e.g., Frontend Developer, Data Engineer"
                        onChange={handleChange}
                        required
                    />
                </div>

                <div className={styles.formGroup}>
                    <label className={styles.label} htmlFor="uk_location">Locations (Max 3)</label>
                    <Select
                        isMulti
                        name="uk_location"
                        options={ukCities}
                        value={ukCities.filter(option => formData.uk_location.includes(option.value))}
                        onChange={(selected) => handleMultiSelectChange(selected, "uk_location", MAX_LOCATIONS)}
                        isOptionDisabled={() => formData.uk_location.length >= MAX_LOCATIONS}
                        placeholder="Select locations..."
                        isClearable
                        isSearchable
                        styles={selectStyles}
                    />
                </div>

                <div className={styles.formGroup}>
                    <label className={styles.label} htmlFor="date_posted">Posted Within</label>
                    <Select
                        name="date_posted"
                        options={datePostedOptions}
                        value={datePostedOptions.find(option => option.value === formData.date_posted)}
                        onChange={(selected) => setFormData(prev => ({
                            ...prev,
                            date_posted: selected ? selected.value : ""
                        }))}
                        styles={selectStyles}
                        placeholder="All time"
                    />
                </div>

                <div className={styles.formGroup}>
                    <label className={styles.label}>Employment Type (Max 2)</label>
                    <Select
                        name="employment_types"
                        options={jobOptions}
                        value={jobOptions.filter(option => formData.employment_types.includes(option.value))}
                        onChange={(selected) => handleMultiSelectChange(selected, "employment_types", MAX_EMP_TYPES)}
                        isOptionDisabled={() => formData.employment_types.length >= MAX_EMP_TYPES}
                        isMulti
                        isClearable
                        isSearchable
                        styles={selectStyles}
                        placeholder="Select employment types..."
                    />
                </div>

                <div className={styles.formGroup}>
                    <label className={styles.checkboxGroup}>
                        <input
                            className={styles.checkbox}
                            id="hybrid_or_remote"
                            name="hybrid_or_remote"
                            type="checkbox"
                            checked={formData.hybrid_or_remote}
                            onChange={handleChange}
                        />
                        <span className={styles.checkboxLabel}>Remote / Hybrid only</span>
                    </label>
                </div>

                <button className={styles.submitBtn} type="submit">
                    Generate Project Ideas
                </button>
            </form>

            {recentSearches.length > 0 && (
                <div className={styles.recentSection}>
                    <h3 className={styles.sectionTitle}>Recent Searches</h3>
                    <div className={styles.recentList}>
                        {recentSearches.map((search) => {
                            const params = search.parameters;
                            const locations = params.uk_locations?.join(", ") || "All locations";
                            const displayText = `${params.role} • ${locations}`;
                            
                            return (
                                <Link 
                                    className={styles.recentItem}
                                    key={search.job_search_id}
                                    to={`/project-ideas/${search.job_search_id}`}
                                    onClick={() => {
                                        sessionStorage.setItem("activeJobSearchId", search.job_search_id);
                                    }}
                                >
                                    {displayText}
                                </Link>
                            );
                        })}
                    </div>
                </div>
            )}
        </div>
    )
}

export default InitForm;