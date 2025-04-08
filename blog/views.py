from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef
from .forms import QuestionAnswerForm,QuestionForm
from .models import QuestionData, QuestionAnswerData,QuestionLikesData

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')


def index(request):
    return render(request, 'blog/index.html')


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('_list_question')
    else:
        form = QuestionForm()
    return render(request, 'blog/create_question.html', {'form': form})


@login_required
def all_questions_list(request):
    questions = QuestionData.objects.prefetch_related(
        'question_answer', 'question_like'
    ).exclude(user=request.user).order_by('-created')
    
     # Attach a flag to each question
    for q in questions:
        q.liked_by_user = q.question_like.filter(liked_by=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'blog/list_question.html', {'questions': questions,'user_wise':False})

@login_required
def user_wise_questions_list(request):
    questions = QuestionData.objects.prefetch_related(
        'question_answer', 'question_like'
    ).filter(user=request.user).order_by('-created')
    
    return render(request, 'blog/list_question.html', {'questions': questions,'user_wise':True})

@login_required
def post_answer(request, question_id):
    question = get_object_or_404(QuestionData, pk=question_id)

    if request.method == 'POST':
        form = QuestionAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.commented_by = request.user
            answer.save()
            return redirect('_list_question')  # Update based on your view name
    else:
        form = QuestionAnswerForm()

    return render(request, 'blog/post_answer.html', {
        'form': form,
        'question': question
    })


@login_required
def like_answer(request, question_id):
    question = get_object_or_404(QuestionData, pk=question_id)
    # Optional: Prevent duplicate likes from the same user
    already_liked = QuestionLikesData.objects.filter(question=question, liked_by=request.user).exists()
    if not already_liked:
        QuestionLikesData.objects.create(question=question, liked_by=request.user)
    else:
        QuestionLikesData.objects.filter(question=question, liked_by=request.user).delete()

    return redirect('_list_question')  # Or redirect to detail page if you have one