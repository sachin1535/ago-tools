import sys
sys.path.append(r"..")
from agoTools.admin import Admin
try:
    ##1) Enter ago org admin credentials below######
    adminUsername = "CenterSpatialStudiesUoR"
    adminPassword = "Redlands!1"
    ##2) Update & overwrite licenses for everyone or just assign to users with no current entitlements
    overwriteAll = False
    ##3) Modify licensing options in userEntitlements list if necessary.######
    ##PRO (pick one):
    ##  Basic = desktopBasicN
    ##  Standard = destkopStdN
    ##  Advanced = desktopAdvN
    ##Extensions (add all that apply):
    ##   Spatial Analyst = SpatialAnalystN
    ##   3D Analyst = 3DAnalystN
    ##   Network Analyst = 3DnetworkAnalystN
    ##   Geostatistical Analyst = geostatAnalystN
    ##   Data Reviewer: dataReviewerN
    ##   Workflow Manager: workflowMgrN
    ##   Data Interoperability: dataInteropN
    ####################################
    userEntitlements = ["desktopAdvN","3DAnalystN","dataReviewerN","geostatAnalystN","networkAnalystN","spatialAnalystN","workflowMgrN","dataInteropN"]


    agoAdmin = Admin(adminUsername,password=adminPassword)

    users = agoAdmin.getUsers()
    ents = agoAdmin.getEntitlements()
    newUsers = []
    for user in users:
        if overwriteAll == False:
            found = False
            for ent in ents:
                if user["username"] == ent["username"]:
                    found = True
                    break
            if found == False:
                newUsers.append(user)
           ## print user["username"]
        else:
            newUsers.append(user)

    response= agoAdmin.setEntitlements(newUsers,userEntitlements)
    print response
except:
    print "error"
