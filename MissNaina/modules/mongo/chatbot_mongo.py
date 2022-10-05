from MissNaina import mongodb as db_x

himawari = db_x["CHATBOT"]


def add_chat(chat_id):
    hima = himawari.find_one({"chat_id": chat_id})
    if hima:
        return False
    himawari.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    hima = himawari.find_one({"chat_id": chat_id})
    if not hima:
        return False
    himawari.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(himawari.find())
    if r:
        return r
    return False


def get_session(chat_id):
    hima = himawari.find_one({"chat_id": chat_id})
    if not hima:
        return False
    return hima
