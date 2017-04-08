from flask import Blueprint, render_template


twitter_blueprint = Blueprint('twitter_view', __name__)


@twitter_blueprint.route('/twitter', methods=['GET', 'POST'])
def index():
    return render_template('twitter/index.html')
