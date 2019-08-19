# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-18 18:05:34
# =============================================================================

class dev_table(db.Model):
    __tablename__ = 'Dev_Tables'
    Id                        = db.Column( db.Integer, primary_key=True, autoincrement=True )
    Name                      = db.Column( db.String(45) )
    Caption                   = db.Column( db.String(45) )
    Entity                    = db.Column( db.String(45) )
    Class_Name                = db.Column( db.String(45) )
    Child_Table               = db.Column( db.String(45) )
    Parent_Table              = db.Column( db.String(45) )
    Use_Pagination            = db.Column( db.Boolean )
    Use_Children_Pagination   = db.Column( db.Boolean )
    Generate_Form_One         = db.Column( db.Boolean )
    Generate_Form_All         = db.Column( db.Boolean )
    Generate_Form_Filter      = db.Column( db.Boolean )
    Generate_Children         = db.Column( db.Boolean )
    Generate_Foreign_Fields   = db.Column( db.Boolean )
    Permission_View           = db.Column( db.Boolean )
    Permission_Delete         = db.Column( db.Boolean )
    Permission_Modify         = db.Column( db.Boolean )
    Permission_Report         = db.Column( db.Boolean )
    Permission_Export         = db.Column( db.Boolean )
    Permission_View_Private   = db.Column( db.Boolean )
    Permission_Modify_Private = db.Column( db.Boolean )
    Permission_Administer     = db.Column( db.Boolean )


    def __init__(self, Id=0, Name='None', Caption='None', Entity='None', Class_Name='None', Child_Table='None', Parent_Table='None', Use_Pagination=None, Use_Children_Pagination=None, Generate_Form_One=None, Generate_Form_All=None, Generate_Form_Filter=None, Generate_Children=None, Generate_Foreign_Fields=None, Permission_View=None, Permission_Delete=None, Permission_Modify=None, Permission_Report=None, Permission_Export=None, Permission_View_Private=None, Permission_Modify_Private=None, Permission_Administer=None):
        self.Id                        = Id
        self.Name                      = Name
        self.Caption                   = Caption
        self.Entity                    = Entity
        self.Class_Name                = Class_Name
        self.Child_Table               = Child_Table
        self.Parent_Table              = Parent_Table
        self.Use_Pagination            = Use_Pagination
        self.Use_Children_Pagination   = Use_Children_Pagination
        self.Generate_Form_One         = Generate_Form_One
        self.Generate_Form_All         = Generate_Form_All
        self.Generate_Form_Filter      = Generate_Form_Filter
        self.Generate_Children         = Generate_Children
        self.Generate_Foreign_Fields   = Generate_Foreign_Fields
        self.Permission_View           = Permission_View
        self.Permission_Delete         = Permission_Delete
        self.Permission_Modify         = Permission_Modify
        self.Permission_Report         = Permission_Report
        self.Permission_Export         = Permission_Export
        self.Permission_View_Private   = Permission_View_Private
        self.Permission_Modify_Private = Permission_Modify_Private
        self.Permission_Administer     = Permission_Administer

    def __repr__(self):
        return "<Dev_Tables( Id='%s', Name='%s', Caption='%s', Entity='%s', Class_Name='%s', Child_Table='%s', Parent_Table='%s', Use_Pagination='%s', Use_Children_Pagination='%s', Generate_Form_One='%s', Generate_Form_All='%s', Generate_Form_Filter='%s', Generate_Children='%s', Generate_Foreign_Fields='%s', Permission_View='%s', Permission_Delete='%s', Permission_Modify='%s', Permission_Report='%s', Permission_Export='%s', Permission_View_Private='%s', Permission_Modify_Private='%s', Permission_Administer='%s')>" % \
                ( self.Id, self.Name, self.Caption, self.Entity, self.Class_Name, self.Child_Table, self.Parent_Table, self.Use_Pagination, self.Use_Children_Pagination, self.Generate_Form_One, self.Generate_Form_All, self.Generate_Form_Filter, self.Generate_Children, self.Generate_Foreign_Fields, self.Permission_View, self.Permission_Delete, self.Permission_Modify, self.Permission_Report, self.Permission_Export, self.Permission_View_Private, self.Permission_Modify_Private, self.Permission_Administer)

