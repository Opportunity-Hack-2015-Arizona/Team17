from main.api_connectors.dropbox_connect import DropboxConnect

basic = Blueprint('basic', __name__)

# @basic.route("/", methods=["GET", "POST"])
# def index():
# 	if request.method == "POST":

@basic.route("/course_content")
def get_course_content():
	name = request.args.get("username")
	dropbox = DropboxConnect()
	course = "Full Term"
	return dropbox.get_content_hierarchy("/"+course)

@basic.route("/get_file")
def get_file():
	filepath = request.args.get("filepath")
	dropbox = DropboxConnect()
	return {"filepath": dropbox.get_file(filepath)}