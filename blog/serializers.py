from rest_framework import serializers
from .models import Article, ArticleText, ArticleImage, Tag, Category, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'count']

    count = serializers.SerializerMethodField(read_only=True)

    def get_count(self, obj):
        return obj.article_set.count()


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title']


class MiniImagaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['id', 'image', 'is_vite']


class MiniTextSerializers(serializers.ModelSerializer):
    subpicture = MiniImagaSerializers(read_only=True, many=True)
    class Meta:
        model = ArticleText
        fields = ['id', 'article', 'description', 'subpicture']


class MiniCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']


# class ArticleImageSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleImage
#         fields = ['id', 'article_text', 'image', 'is_vite']


class ArticleGetSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    tags = TagSerializers(read_only=True, many=True)
    article_text = MiniTextSerializers(read_only=True)
    comments = MiniCommentSerializers(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'article_text', 'category', 'tags',
                  'comments', 'views', 'created_date']


class ArticlePOSTSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'tags', 'views', 'created_date']


class CommentSerializer(serializers.ModelSerializer):
    article = MiniArticleSerializers(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']

        extra_kwargs = {
            "article": {'required': False},
        }

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile_user.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['id', 'article_text', 'image', 'is_vite']
    #
    # def create(self, validated_data):
    #     article_text_id = self.context['article_text_id']
    #     image = validated_data.get('image')
    #     instance = ArticleImage.objects.create(article_text_id=article_text_id, image=image)
    #     return instance


class SubTextSerializer(serializers.ModelSerializer):
    subpicture = MiniImagaSerializers(read_only=True, many=True)

    class Meta:
        model = ArticleText
        fields = ['id', 'article', 'description', 'subpicture']

        extra_kwargs = {
            "article": {'required': False},
        }
    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        description = validated_data.get('description')
        instance = ArticleText.objects.create(article_id=article_id, description=description)
        return instance


