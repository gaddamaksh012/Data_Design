from turtle import update
import psycopg2
import psycopg2.extras

filename = "MyConfig.config"
contents = open(filename).read()
config = eval(contents)

hostname = config["hostname"]
database = config["database"]
username =  config["username"]
pwd = config["pwd"]
port_id = config["port_id"]

try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port =port_id
        ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS akash_details')
            create_script = ''' CREATE TABLE akash_details(

                id int PRIMARY KEY,
                name varchar(40),
                salary int, 
                dept_id varchar(30)

            )'''
            cur.execute(create_script)


            insert_script = 'INSERT INTO akash_details (id,name,salary,dept_id) values(%s,%s,%s,%s)'
            insert_values = [(10,"Ridhu",20000,"Mech"),(20,"Gaddam",30000,"CSR")]


            for record in insert_values:
                cur.execute(insert_script,record)


            cur.execute('SELECT * FROM akash_details')
            for record in cur.fetchall():
                # print(record['name'],record['dept_id'])
                print(record)


            update_script = 'update akash_details set salary = salary + (salary*0.5)'
            cur.execute(update_script)


            delet_sript = "delete from akash_details where name = %s"
            delete_record = ("Gaddam",)
            cur.execute(delet_sript,delete_record) 


            conn.commit()

except Exception as e:
    print("error is {}".format(e))

else:
    conn.close()
    print("it's working fine")


