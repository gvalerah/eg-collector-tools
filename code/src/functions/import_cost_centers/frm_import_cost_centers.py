# =============================================================================
# Export User Resume FORM
# (c) Sertechno 2019
# GLVH @ 2019-01-05
# =============================================================================

# =============================================================================
from flask_wtf.file import FileField,FileRequired,FileAllowed

class frm_import_cost_centers(Form):
    Import          = FileField ("Import Cost Centers Data?", validators=[FileRequired(), FileAllowed(['xls'],'XLS Spreadsheets only!!!')])



