import bcrypt as bc

def validate_password(password, hashed_pw):
    hashed_pw = hashed_pw.encode('utf-8')
    return bc.checkpw(password.encode('utf-8'), hashed_pw)
