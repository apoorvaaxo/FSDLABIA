from django.shortcuts import render

def display_lists(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Pineapple']
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    context = {
        'fruits': fruits,
        'students': students,
    }
    return render(request, 'display_lists.html', context)
