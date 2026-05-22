"""Theme and styling module for ReminderEDU"""

class CSSTheme:
    """Centralized CSS theme generator with all styling logic in Python"""
    
    # Color variables
    COLORS = {
        'primary_start': '#667eea',
        'primary_end': '#764ba2',
        'glass_bg': 'rgba(255, 255, 255, 0.85)',
        'glass_border': 'rgba(255, 255, 255, 0.5)',
        'text_main': '#2d3436',
        'text_sub': '#636e72',
        'danger': '#ff4757',
        'safe': '#2ecc71',
        'warning': '#ffa502',
        'urgent': '#ff6b6b',
    }
    
    # Urgency levels with colors
    URGENCY_COLORS = {
        4: '#c0392b',  # Overdue - Dark red
        3: '#e74c3c',  # Due Soon - Red
        2: '#e67e22',  # Today - Orange
        1: '#f1c40f',  # Upcoming - Yellow
        0: '#2ecc71',  # Planned - Green
    }
    
    STATUS_COLORS = {
        4: '#c0392b',
        3: '#e74c3c',
        2: '#e67e22',
        1: '#b7950b',
        0: '#27ae60',
    }
    
    @staticmethod
    def generate_css():
        """Generate complete CSS from Python configuration"""
        css = f"""
:root {{
    --primary-gradient: linear-gradient(135deg, {CSSTheme.COLORS['primary_start']} 0%, {CSSTheme.COLORS['primary_end']} 100%);
    --glass-bg: {CSSTheme.COLORS['glass_bg']};
    --glass-border: {CSSTheme.COLORS['glass_border']};
    --text-main: {CSSTheme.COLORS['text_main']};
    --text-sub: {CSSTheme.COLORS['text_sub']};
    --danger: {CSSTheme.COLORS['danger']};
    --safe: {CSSTheme.COLORS['safe']};
    --warning: {CSSTheme.COLORS['warning']};
    --urgent: {CSSTheme.COLORS['urgent']};
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    color: var(--text-main);
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
}}

.bg-shape {{
    position: fixed;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.6;
    z-index: -1;
}}

.shape-1 {{
    height: 400px;
    width: 400px;
    background: #764ba2;
    top: -100px;
    left: -100px;
    animation: float 8s ease-in-out infinite;
}}

.shape-2 {{
    height: 300px;
    width: 300px;
    background: #667eea;
    bottom: -50px;
    right: -50px;
    animation: float 6s ease-in-out infinite reverse;
}}

.shape-3 {{
    height: 200px;
    width: 200px;
    background: #ff9ff3;
    top: 40%;
    left: 50%;
    animation: float 10s ease-in-out infinite;
}}

@keyframes float {{
    0% {{ transform: translate(0, 0); }}
    50% {{ transform: translate(30px, 30px); }}
    100% {{ transform: translate(0, 0); }}
}}

.container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

header {{
    text-align: center;
    margin-bottom: 40px;
}}

h1 {{
    font-size: 2.5rem;
    color: #2d3436;
    font-weight: 700;
    margin-bottom: 5px;
    letter-spacing: -1px;
}}

p {{
    color: var(--text-sub);
    font-weight: 300;
}}

.card-glass {{
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
    border-radius: 20px;
}}

.input-section {{
    padding: 30px;
    margin-bottom: 40px;
}}

.schedule-form {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}}

.form-group {{
    display: flex;
    flex-direction: column;
}}

.form-group label {{
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-sub);
    margin-bottom: 5px;
    text-transform: uppercase;
}}

input[type="text"], input[type="date"], input[type="time"] {{
    background: rgba(255, 255, 255, 0.6);
    border: 1px solid rgba(0,0,0,0.05);
    padding: 12px 15px;
    border-radius: 10px;
    font-family: 'Poppins', sans-serif;
    font-size: 0.95rem;
    transition: all 0.3s;
}}

input:focus {{
    outline: none;
    background: white;
    box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.2);
}}

.horizontal {{
    grid-column: span 2;
    display: flex;
    gap: 20px;
}}

.date-picker, .time-picker {{
    flex: 1;
}}

.add-btn {{
    grid-column: span 2;
    padding: 15px;
    background: var(--primary-gradient);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}}

.add-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(118, 75, 162, 0.3);
}}

.schedule-list {{
    display: flex;
    flex-direction: column;
    gap: 20px;
}}

.task-card {{
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    padding: 20px;
    transition: transform 0.2s;
    position: relative;
    overflow: hidden;
}}

.task-card::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 6px;
}}
"""
    
    # Add urgency color rules
    for urgency, color in CSSTheme.URGENCY_COLORS.items():
        css += f".urgency-{urgency}::before {{ background: {color}; }}\n"
    
    css += """
.task-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

.task-main {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.task-info {
    flex: 1;
}

.task-top {
    display: flex;
    gap: 10px;
    margin-bottom: 5px;
}

.subject-badge {
    font-size: 0.75rem;
    background: #f1f2f6;
    padding: 4px 10px;
    border-radius: 20px;
    color: #636e72;
    font-weight: 600;
}

.status-badge {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
}
"""
    
    # Add status color rules
    for status, color in CSSTheme.STATUS_COLORS.items():
        css += f".status-{status} {{ color: {color}; }}\n"
    
    css += """
.task-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin: 5px 0;
    color: #2d3436;
}

.task-datetime {
    display: flex;
    gap: 15px;
    font-size: 0.9rem;
    color: #7f8c8d;
}

.task-action {
    text-align: right;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
}

.countdown {
    font-weight: 700;
    font-size: 1.1rem;
    color: #2d3436;
}

.delete-btn {
    background: transparent;
    border: none;
    color: #b2bec3;
    cursor: pointer;
    padding: 5px;
    transition: color 0.2s;
}

.delete-btn:hover {
    color: var(--danger);
    transform: scale(1.1);
}

.empty-state {
    text-align: center;
    padding: 40px;
    background: white;
    border-radius: 16px;
}

.empty-img {
    width: 100px;
    opacity: 0.8;
    margin-bottom: 15px;
}

@media (max-width: 600px) {
    .schedule-form {
        grid-template-columns: 1fr;
    }

    .horizontal {
        grid-column: span 1;
        flex-direction: column;
    }

    .add-btn {
        grid-column: span 1;
    }

    .task-main {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
    }

    .task-action {
        flex-direction: row;
        width: 100%;
        justify-content: space-between;
        align-items: center;
    }
}
"""
    return css
