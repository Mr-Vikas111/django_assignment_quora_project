from django.db import models
from users.models import User
from helper.models import BaseModel

# UserPost Model

class QuestionData(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    question = models.TextField()
    
    def __str__(self):
        return f"{self.question}"

class QuestionAnswerData(BaseModel):
    question = models.ForeignKey(QuestionData,on_delete=models.CASCADE,related_name="question_answer")
    answer = models.TextField()
    commented_by = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="question_answer_user", null=True)

    def __str__(self):
        return f"{self.id} Que. {self.question}, Ans. {self.answer}"

class QuestionLikesData(BaseModel):
    question = models.ForeignKey(QuestionData,on_delete=models.CASCADE,related_name="question_like")
    liked_by = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="question_like", null=True)
    
    def __str__(self):
        return f"{str(self.liked_by)}"