"""
CSS Generator Module - Generates all CSS dynamically from Python
This module defines all styling rules as Python constants and generates CSS on-the-fly
"""

class CSSTheme:
    """Manages all CSS styling through Python"""
    
    # Color Variables
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
        'bg_light': '#f1f2f6',
        'bg_dark': '#7f8c8d',
        'card_shadow': 'rgba(31, 38, 135, 0.1)',
    }
    
    # Urgency Color Mapping
    URGENCY_COLORS = {
        4: '#c0392b',  # Overdue - Dark Red
        3: '#e74c3c',  # Due Soon - Red
        2: '#e67e22',  # Today - Orange
        1: '#f1c40f',  # Upcoming - Yellow
        0: '#2ecc71',  # Planned - Green
    }
    
    # Gradients
    GRADIENTS = {
        'primary': f"linear-gradient(135deg, {COLORS['primary_start']} 0%, {COLORS['primary_end']} 100%)",
        'background': "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
    }
    
    # Shape Animations
    SHAPES = [
        {'size': 400, 'bg': '#764ba2', 'top': '-100px', 'left': '-100px', 'duration': '8s', 'direction': 'normal'},
        {'size': 300, 'bg': '#667eea', 'bottom': '-50px', 'right': '-50px', 'duration': '6s', 'direction': 'reverse'},
        {'size': 200, 'bg': '#ff9ff3', 'top': '40%', 'left': '50%', 'duration': '10s', 'direction': 'normal'},
    ]
    
    @classmethod
    def generate_css(cls):
        """Generate complete CSS as a string"""
        css_parts = []
        
        # CSS Variables
        css_parts.append(cls._generate_root())
        
        # Reset & Base Styles
        css_parts.append(cls._generate_base_styles())
        
        # Background Shapes
        css_parts.append(cls._generate_shape_styles())
        
        # Layout & Container
        css_parts.append(cls._generate_layout_styles())
        
        # Form & Input Styles
        css_parts.append(cls._generate_form_styles())
        
        # Task Card Styles
        css_parts.append(cls._generate_task_styles())
        
        # Empty State
        css_parts.append(cls._generate_empty_state())
        
        # Responsive Design
        css_parts.append(cls._generate_responsive())
        
        # Animations
        css_parts.append(cls._generate_animations())
        
        return '\n'.join(css_parts)
    
    @classmethod
    def _generate_root(cls):
        """Generate CSS root variables"""
        return f"""
:root {{
    --primary-gradient: {cls.GRADIENTS['primary']};
    --glass-bg: {cls.COLORS['glass_bg']};
    --glass-border: {cls.COLORS['glass_border']};
    --text-main: {cls.COLORS['text_main']};
    --text-sub: {cls.COLORS['text_sub']};
    --danger: {cls.COLORS['danger']};
    --safe: {cls.COLORS['safe']};
    --warning: {cls.COLORS['warning']};
    --urgent: {cls.COLORS['urgent']};
}}
"""
    
    @classmethod
    def _generate_base_styles(cls):
        """Generate base element styles"""
        return f"""
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
    background: {cls.GRADIENTS['background']};
    color: {cls.COLORS['text_main']};
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
}}

h1 {{
    font-size: 2.5rem;
    color: {cls.COLORS['text_main']};
    font-weight: 700;
    margin-bottom: 5px;
    letter-spacing: -1px;
}}

p {{
    color: {cls.COLORS['text_sub']};
    font-weight: 300;
}}
"""
    
    @classmethod
    def _generate_shape_styles(cls):
        """Generate background shape styles"""
        shape_css = []
        shape_css.append("""
.bg-shape {
    position: fixed;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.6;
    z-index: -1;
}
""")
        
        for idx, shape in enumerate(cls.SHAPES, 1):
            animation = f"float {shape['duration']} ease-in-out infinite {shape['direction']}"
            pos = f"top: {shape['top']}; left: {shape['left']};" if 'top' in shape else \
                  f"bottom: {shape['bottom']}; right: {shape['right']};"
            
            shape_css.append(f"""
.shape-{idx} {{
    height: {shape['size']}px;
    width: {shape['size']}px;
    background: {shape['bg']};
    {pos}
    animation: {animation};
}}
""")
        
        return ''.join(shape_css)
    
    @classmethod
    def _generate_layout_styles(cls):
        """Generate layout and container styles"""
        return f"""
.container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

header {{
    text-align: center;
    margin-bottom: 40px;
}}

.card-glass {{
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    box-shadow: 0 8px 32px 0 {cls.COLORS['card_shadow']};
    border-radius: 20px;
}}

.input-section {{
    padding: 30px;
    margin-bottom: 40px;
}}
"""
    
    @classmethod
    def _generate_form_styles(cls):
        """Generate form and input styles"""
        return f"""
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
    color: {cls.COLORS['text_sub']};
    margin-bottom: 5px;
    text-transform: uppercase;
}}

input[type="text"], input[type="date"], input[type="time"] {{
    background: rgba(255, 255, 255, 0.6);
    border: 1px solid rgba(0,0,0,0.05);
    padding: 12px 15px;
    border-radius: 10px;
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
"""
    
    @classmethod
    def _generate_task_styles(cls):
        """Generate task card styles with urgency levels"""
        task_css = f"""
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
        
        # Add urgency color styles
        for urgency, color in cls.URGENCY_COLORS.items():
            task_css += f"""
.urgency-{urgency}::before {{ background: {color}; }}
.status-{urgency} {{ color: {color}; }}
"""
        
        task_css += f"""
.task-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}}

.task-main {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.task-info {{
    flex: 1;
}}

.task-top {{
    display: flex;
    gap: 10px;
    margin-bottom: 5px;
}}

.subject-badge {{
    font-size: 0.75rem;
    background: {cls.COLORS['bg_light']};
    padding: 4px 10px;
    border-radius: 20px;
    color: {cls.COLORS['text_sub']};
    font-weight: 600;
}}

.status-badge {{
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
}}

.task-title {{
    font-size: 1.2rem;
    font-weight: 600;
    margin: 5px 0;
    color: {cls.COLORS['text_main']};
}}

.task-datetime {{
    display: flex;
    gap: 15px;
    font-size: 0.9rem;
    color: {cls.COLORS['bg_dark']};
}}

.task-action {{
    text-align: right;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
}}

.countdown {{
    font-weight: 700;
    font-size: 1.1rem;
    color: {cls.COLORS['text_main']};
}}

.delete-btn {{
    background: transparent;
    border: none;
    color: #b2bec3;
    cursor: pointer;
    padding: 5px;
    transition: color 0.2s;
}}

.delete-btn:hover {{
    color: {cls.COLORS['danger']};
    transform: scale(1.1);
}}
"""
        return task_css
    
    @classmethod
    def _generate_empty_state(cls):
        """Generate empty state styles"""
        return f"""
.empty-state {{
    text-align: center;
    padding: 40px;
    background: white;
    border-radius: 16px;
}}

.empty-icon {{
    width: 100px;
    opacity: 0.8;
    margin-bottom: 15px;
}}
"""
    
    @classmethod
    def _generate_responsive(cls):
        """Generate responsive design styles"""
        return """
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
    
    @classmethod
    def _generate_animations(cls):
        """Generate animation keyframes"""
        return """
@keyframes float {
    0% { transform: translate(0, 0); }
    50% { transform: translate(30px, 30px); }
    100% { transform: translate(0, 0); }
}
"""
