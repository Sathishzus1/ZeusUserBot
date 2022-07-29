from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 530164
    API_HASH = "8b4ab08165f1fa5b70350824ab8a78a6"
    # the name to display in your alive message
    ALIVE_NAME = "ST1SELF"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://zzsnrdki:aFPyBl53Yocu_4HNoOm7jfQvWQhaMt4d@kandula.db.elephantsql.com/zzsnrdki"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBu41h0-8xOKNdl2n3LyPO7QU1YXDw2yTCMRQLOv76RnTME-rAiatWIsxvlvASXINr7puKq92Eon9fsZzcG6dKbGLdc637_fGrQII-78xv9GdYR15Ba-ajyzUaQnW4vvfk0ArI7Mck0AS59u9e3m_ri8D15L49RXXLk07jgv2ETr4xNiwPIDNNQivpsrRqFeZ_hDYjE_qR5T4DmsVmGesJtzgENo2lG56O8JraXX7ovCE76N00xsxjTZHf86GIe-RDj_Umnq9DCXoWiIqOp4XPgqc7dLpnsKIf6IJUlLFxjm89ndbJ0hvyBFtLNl-GRO3TRD-QRlAkT6Kx-Do-PmKWtu0="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5599412897:AAETaitCjt9d_mVvfgotwAoN0gvO3RMLPb0"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
