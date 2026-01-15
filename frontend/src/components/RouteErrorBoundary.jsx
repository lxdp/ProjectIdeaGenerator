import { useRouteError, useNavigate } from 'react-router-dom';

function RouteErrorBoundary() {
    const error = useRouteError();
    const navigate = useNavigate();

    console.error('Route error:', error);

    return (
        <div style={{
            minHeight: '100vh',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px',
            background: 'var(--bg-primary)',
            color: 'var(--text-primary)'
        }}>
            <div style={{
                maxWidth: '500px',
                textAlign: 'center',
                padding: 'var(--spacing-xl)',
                background: 'var(--bg-secondary)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--border-color)'
            }}>
                <h2 style={{
                    fontSize: '1.5rem',
                    marginBottom: 'var(--spacing-md)',
                    color: 'var(--text-primary)'
                }}>
                    Something went wrong
                </h2>
                
                <p style={{
                    color: 'var(--text-secondary)',
                    marginBottom: 'var(--spacing-lg)',
                    lineHeight: '1.6'
                }}>
                    {error?.message || 'An unexpected error occurred. Please try again.'}
                </p>

                <div style={{ display: 'flex', gap: 'var(--spacing-md)', justifyContent: 'center' }}>
                    <button
                        onClick={() => navigate(-1)}
                        style={{
                            padding: 'var(--spacing-sm) var(--spacing-lg)',
                            background: 'transparent',
                            border: '1px solid var(--border-color)',
                            color: 'var(--text-primary)',
                            borderRadius: 'var(--radius-md)',
                            cursor: 'pointer'
                        }}
                    >
                        Go Back
                    </button>
                    
                    <button
                        onClick={() => navigate('/')}
                        style={{
                            padding: 'var(--spacing-sm) var(--spacing-lg)',
                            background: 'var(--accent-primary)',
                            border: 'none',
                            color: 'var(--bg-primary)',
                            borderRadius: 'var(--radius-md)',
                            cursor: 'pointer',
                            fontWeight: '600'
                        }}
                    >
                        Go Home
                    </button>
                </div>

                {process.env.NODE_ENV === 'development' && error?.stack && (
                    <details style={{
                        marginTop: 'var(--spacing-xl)',
                        textAlign: 'left',
                        background: 'var(--bg-card)',
                        padding: 'var(--spacing-md)',
                        borderRadius: 'var(--radius-md)',
                        fontSize: '0.85rem'
                    }}>
                        <summary style={{ cursor: 'pointer', color: 'var(--text-muted)' }}>
                            Error Details (Development)
                        </summary>
                        <pre style={{
                            marginTop: 'var(--spacing-sm)',
                            whiteSpace: 'pre-wrap',
                            wordBreak: 'break-word',
                            color: 'var(--text-secondary)'
                        }}>
                            {error.stack}
                        </pre>
                    </details>
                )}
            </div>
        </div>
    );
}

export default RouteErrorBoundary;

