from flask import Blueprint, render_template, request

from .forms import TwitterForm
from .twitterAPI import getTweets

twitter_blueprint = Blueprint('twitter_view', __name__)


@twitter_blueprint.route('/twitter', methods=['GET', 'POST'])
def index():
    form = TwitterForm(request.form)
    if request.method == 'POST':
        # The form was submitted
        username = form.username.data # This is what the user typed
        tweets = getTweets(username)
        if tweets:
            return render_template('twitter/tweets.html',
                                   tweets=tweets,
                                   username=username,)
        return 'Invalid username. Sorry :('
    return render_template('twitter/index.html', form=form)


@twitter_blueprint.route('/how')
def how():
    return render_template('twitter/how.html')
