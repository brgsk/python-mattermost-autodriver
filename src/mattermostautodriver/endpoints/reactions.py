from .base import Base


class Reactions(Base):
    def save_reaction(self, options):
        """Create a reaction
        `Read in Mattermost API docs (reactions - SaveReaction) <https://api.mattermost.com/#tag/reactions/operation/SaveReaction>`_
        """
        return self.client.post("""/reactions""", options=options)

    def get_reactions(self, post_id):
        """Get a list of reactions to a post

        post_id: ID of a post

        `Read in Mattermost API docs (reactions - GetReactions) <https://api.mattermost.com/#tag/reactions/operation/GetReactions>`_
        """
        return self.client.get(f"/posts/{post_id}/reactions")

    def delete_reaction(self, user_id, post_id, emoji_name):
        """Remove a reaction from a post

        user_id: ID of the user
        post_id: ID of the post
        emoji_name: emoji name

        `Read in Mattermost API docs (reactions - DeleteReaction) <https://api.mattermost.com/#tag/reactions/operation/DeleteReaction>`_
        """
        return self.client.delete(f"/users/{user_id}/posts/{post_id}/reactions/{emoji_name}")

    def get_bulk_reactions(self, options):
        """Bulk get the reaction for posts
        `Read in Mattermost API docs (reactions - GetBulkReactions) <https://api.mattermost.com/#tag/reactions/operation/GetBulkReactions>`_
        """
        return self.client.post("""/posts/ids/reactions""", options=options)
