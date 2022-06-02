from myapp import app
import os

p = os.environ.get('PORT')
p = p if p else '5055'

if __name__ == '__main__':


    print(f"-- DEBUG MODE ----  -----")
    # app.run(debug=True, port=p)
    
    # print("-- TESTING MODE ----")
    # app.run(debug=False, port=p)
    # app.after_request(sql_debug)

