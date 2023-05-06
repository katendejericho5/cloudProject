document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      // options go here
    });
    calendar.render();
  });
  
  events: [
  {
    title: 'Task 1',
    start: '2023-05-02'
  },
  {
    title: 'Task 2',
    start: '2023-05-03'
  }
],
eventColor: '#3788d8',
eventTextColor: 'white',

// Add a new event to the calendar
calendar.addEvent({
  title: 'New Task',
  start: '2023-05-04'
});

// Update an existing event
var event = calendar.getEventById('event-id');
event.setProp('title', 'New Title');
event.setStart('2023-05-05');
event.setEnd('2023-05-07');
