
"""
Local Settings for development that consist of sensitive data
and should not go to the git repo
"""

# Email Settings
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
DEFAULT_FROM_EMAIL = 'Calorie Counter <noreply@caloriecaunter.com>'
SERVER_EMAIL = 'noreply@caloriecaunter.mk'