/**
 * Created by user1 on 05.11.2014.
 */



$(document).ready(function() {
    var things = JSON.parse(localStorage.getItem("es.esy.akhtyamovpavel.todolist"));
    for (var i in things) {
        addTask(things[i]);
    }
    updateCounter();

    $("#todo-input").submit(function(e) {
        if (e.preventDefault()) {
            e.preventDefault();
        }
        var text = $('#add-todo').val();
        if (text != "") {
            addTask(text);
        }
        $('#add-todo').val("");
        updateCounter();
    });

    $("#switch-all").change(function() {
        var tasks = $('input[type="checkbox"]');
        if (!$(this).prop('checked')) {
            for (var i = 0; i < tasks.length; ++i) {
                if (tasks[i] != this) {
                    $(tasks[i]).prop('checked', false);
                    var to_change = $(tasks[i]).siblings()[0];
                    $(to_change).css('text-decoration', 'none');
                }

            }
            $("#remove-all-tasks").css('display', 'none');
        }
        else {
            for (var i = 0; i < tasks.length; ++i)  {
                if (tasks[i] != this) {
                    $(tasks[i]).prop('checked', true);
                    var to_change = $(tasks[i]).siblings()[0];
                    $(to_change).css('text-decoration',  'line-through');
                }
            }
            $("#remove-all-tasks").css('display', 'block');
        }

        updateCounter();
    });

    $("#remove-all-tasks").click(function() {
        var tasks = $($('input[class="switch-task"]:checked'));
        for (var i = 0; i < tasks.length; ++i) {
            var c = $($($(tasks[i]).parent()).parent()).remove();
            $(c).remove();
        }
        $("#remove-all-tasks").css('display', 'none');
        $("#switch-all").prop('checked', false);
        updateCounter();
    });

    $(document).on('dblclick', '.task', function() {
        var childTag = $($(this).children()[0]);
        var childInput = $($(this).children()[1]);
        childTag.css('display', 'none');
        var text = $(childTag.children()[1]).text();
        var ttt = $(childInput.children()[0]);
        console.log(text);
        ttt.val(text);
        childInput.css('display', 'block');
        childInput.children()[0].focus();
        updateCounter();
    });

    $(document).on('mouseover', '.task-view', function() {

        $($(this).children()[2]).css('display', 'inline-block');
    });

    $(document).on('mouseout', '.task-view', function() {
        $($(this).children()[2]).css('display', 'none');
    });


    $(document).on('submit', '.change-edit', function(e) {
        if (e.preventDefault()) {
            e.preventDefault();
        }
        var childView = $($(this).parent().children()[0]);
        var childTag = $(childView.children()[1]);
        var childInput = $($(this).children()[0]);
        childView.css('display', 'block');
        childTag.text(childInput.val());
        console.log(childInput.val());
        $(this).css('display', 'none');
        updateCounter();
    });

    $(document).on('blur', '.change-edit', function() {
        var childView = $($(this).parent().children()[0]);
        var childTag = $(childView.children()[1]);
        var childInput = $($(this).children()[0]);
        childView.css('display', 'block');
        childTag.text(childInput.val());
        console.log(childInput.val());
        $(this).css('display', 'none');
        updateCounter();
    });


    $(document).on('change', '.switch-task', function() {
        if (!$(this).prop('checked')) {
            var to_change = $(this).siblings()[0];
            $(to_change).css('text-decoration', 'none');
        }
        else {
            var to_change = $(this).siblings()[0];
            $(to_change).css('text-decoration',  'line-through');
        }
        updateCounter();
    })

    $(document).on('click', 'i', function() {
        $($(this).parent().parent()).remove();
        updateCounter();
    });
});

function updateCounter() {
    var left = $('input[class="switch-task"]').length - $('input[class="switch-task"]:checked').length;
    var not_left = $('input[class="switch-task"]:checked').length;
    if (left == 1) {
        $("#tasks-remaining").text(left + " task remaining");
    } else {
        $("#tasks-remaining").text(left + " tasks remaining");
    }

    if (not_left > 0) {
        $("#remove-all-tasks").css('display', 'block');
    } else {
        $("#remove-all-tasks").css('display', 'none');
    }

    var tasks = $('a[class="task-text"]').toArray();
    for (i in tasks) {
        tasks[i] = tasks[i].innerHTML;
    }

    localStorage.setItem("es.esy.akhtyamovpavel.todolist", JSON.stringify(tasks));
}



function addTask(text) {
    var new_task = $('<li class="task">');
    var task_view = $('<div class="task-view">');
    var view = $('<input class="switch-task" type="checkbox" value="">');

    task_view.append(view);
    var task_text = $('<a class="task-text">').text(text);
    task_view.append(task_text);
    new_task.append(task_view);
    var icon = $('<i class="fa fa-times">');
    icon.css('display', 'none');
    task_view.append(icon);
    var form = $('<form class="change-edit">');
    var edit = $('<input class="task-edit" type="text" >');
    form.css('display', 'none');
    form.append(edit);
    new_task.append(form);
    $('#list-tasks').append(new_task);
    updateCounter();
}