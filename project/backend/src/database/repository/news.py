import json
import uuid
from bson import json_util 
from bson.objectid import ObjectId
from database.connection import Database

class NewsDAO:
    def __init__(self):
        self.db = Database(database="application", collection="news")

    def get_all(self):
        try:
            response = self.db.collection.find()
            parsed_json = json.loads(json_util.dumps(response))
            return parsed_json
        except Exception as e:
            print(f"Houve um erro ao tentar pegar as notícias: {e}")
            return {"error": "Erro ao pegar notícias"}, 500

    def create(self, new_news):
        id = str(uuid.uuid4())
        new_news.id = id
        try:
            news_json = {
                "id": new_news.id,
                "title": new_news.title,
                "content": new_news.content
            }
            self.db.collection.insert_one(news_json)
            return {"message": "Notícia criada com sucesso"}, 201
        except Exception as e:
            print(f"Houve um erro ao tentar criar uma nova notícia: {e}")
            return {"error": "Erro ao criar notícia"}, 500

    def update(self, news):
        try:
            response = self.db.collection.update_one(
                {"id": news.id},
                {
                    "$set": {
                        "title": news.title,
                        "content": news.content
                    }
                }
            )
            if response.matched_count == 0:
                return {"error": "Notícia não encontrada"}, 404
            else:
                return {"message": "Notícia atualizada com sucesso"}, 200
        except Exception as e:
            print(f"Houve um erro ao tentar atualizar a notícia: {e}")
            return {"error": "Erro ao atualizar notícia"}, 500


    def delete(self, id):
        try:
            response = self.db.collection.delete_one({"id": id})
            print(response.deleted_count)
            if response.deleted_count == 0:
                return {"error": "Notícia não encontrada"}, 404
            else:
                return {"message": "Notícia excluída com sucesso"}, 200
        except Exception as e:
            print(f"Houve um erro ao tentar excluir a notícia: {e}")
            return {"error": "Erro ao excluir notícia"}, 500