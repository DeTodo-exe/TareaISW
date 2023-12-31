from flask import Blueprint
from config import ServerConfig
#We set blueprients routes to modularize api rest
class PatientRoutes:
    #We set patient routes
    p_r = []
    def fetchPatients(self):
        simple_page = Blueprint("fetchPatients",__name__)
        @simple_page.route("/fetchPatients")
        def index():
            return "ajdkaskjdsa"
        self.p_r.append(simple_page)
        return simple_page
    def fetchPatientById(self):
        simple_page = Blueprint("fetchPatientById",__name__)
        @simple_page.route("/fetchPatient/<id>")
        def route(id):
            return f"{id}"
        self.p_r.append(simple_page)
        return simple_page
    def deletePatientById(self):
        simple_page = Blueprint("deletePatientById", __name__)
        @simple_page.route("/deletePatient/<id>")
        def route(id):
            return f"Patient id {id} was deleted"
        self.p_r.append(simple_page)
    def getBlueprints(self):
        #We call Blueprints
        self.fetchPatients()
        self.fetchPatientById()
        self.deletePatientById()
        if (ServerConfig.DEBUG == True):
            #DEBUGGING
            print(f"Total routes created: {len(self.p_r)} {self.p_r}")
        #Return array with blueprints to use in app.py file
        return self.p_r


        

