from flask import request, jsonify
from flask.views import MethodView

from app import app
from validator import validate
from models import User, Post
from schema import POST_CREATE
import errors

class PostsView(MethodView):

    def get(self, post_id=None):
        post = Post.by_id(post_id)
        if not post:
            raise errors.NotFound
        return jsonify(post)

    @validate('json', POST_CREATE)
    def post(self):
        post_positions = [POST_CREATE["properties"].keys()]
        if request.json.keys() not in post_positions:
            raise errors.BadLuck
        post = Post(**request.json)
        post.add()
        return jsonify(post.to_dict())

    def delete(self, post_id=None):
        get = Post.by_id(post_id)
        if not get:
            raise errors.NotFound
        Post.query.filter_by(id=post_id).delete()
        app.db.session.commit()
        return jsonify({"status": "deleted"})


app.add_url_rule('/posts', view_func=PostsView.as_view('posts_get'), methods=['GET', ])
app.add_url_rule('/posts/', view_func=PostsView.as_view('posts_post'), methods=['POST', ])
app.add_url_rule('/posts/<int:post_id>/', view_func=PostsView.as_view('posts_delete'), methods=['DELETE', ])