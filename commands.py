# Stax commands
# ~~~~

import sys

# ~~~~~~~~~~~~~~~~~~~~~~ New
if play_command == 'new':
	appconf = open(os.path.join(application_path, 'conf/application.conf'), 'a')
	appconf.write("\n")
	appconf.write("# Stax Database configuration\n")
	appconf.write("# ~~~~~\n")
	appconf.write("# to deploy on stax: uncomment, replace yourProject, yourDBName, login and password by the correct values\n")
	appconf.write("# and switch to the stax profile before generating the war\n")
	appconf.write("# %stax.db=java:/comp/env/jdbc/yourProject\n\n")
	appconf.write("# %stax.url=jdbc:stax://yourDBName\n")
	appconf.write("# %stax.db.driver=com.staxnet.jdbc.Driver\n")
	appconf.write("# %stax.db.user=login\n")
	appconf.write("# %stax.db.pass=password\n\n")
	appconf.write("# %stax.jpa.dialect=org.hibernate.dialect.MySQLDialect\n")

# ~~~~~~~~~~~~~~~~~~~~~~ War
if play_command == 'war':
	f = open(os.path.join(war_path, 'WEB-INF', 'stax-application.xml'), 'w')
	f.write("<?xml version=\"1.0\"?>\n")
	f.write("        <stax-web-app xmlns=\"http://www.stax.net/xml/webapp/1\">\n")
	f.write("</stax-web-app>")
	print "~\n~ Including Stax declaration..."
	print "~ To deploy your application to Stax, you need to zip it:"
	print "~     jar cvf staxwar -C " + war_path + " ."
	print "~ Then you can deploy it:"
	print "~     stax app:deploy -a login/yourProject staxwar\n~"
