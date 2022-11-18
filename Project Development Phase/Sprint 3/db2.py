import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=/DigiCertGlobalRootCA.crt;UID=scz46320;PWD=nyulIzXaRG4z9nZv;","","")
print("connection successfully")


sql="""CREATE TABLE login (
    Name varchar(255),
    Email varchar(255),
    Password varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)

sql="""CREATE TABLE Customerdetails (
    Name varchar(255),
    ShopName varchar(255),
    Location varchar(255),
    MobileNumber varchar(255) )"""
print("Added successfully")
ibm_db.exec_immediate(conn,sql)


"""{% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, messages in messages %}
          <div class="alert alert-{{category}}" ></div>{{messages}}</div>
        {% endfor %}
  {% endif %}  
  {% endwith %} """