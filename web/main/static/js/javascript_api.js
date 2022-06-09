function toJSONString(form)
{
  var obj = ""
  var elements = form.querySelectorAll('input, select, textarea')
  for (var i = 0; i < elements.length - 1; ++i)
  {
    var element = elements[i]
    var name = element.name
    var value = element.value
    if (name)
    {
      obj += name + ": " + value + " "
    }
  }
  return (obj + "\n")
}

if (form) {
  form.addEventListener('submit', event =>
  {
    event.preventDefault()

	const formId = 'telegramForm'
	const form = document.getElementById("form")
	const token = "5384447081:AAHH-ZVFJE9kbewvd7ip-Cl7_j9ag9Cgrg0"
	const chat_id = "-722018740"
    const json = toJSONString(form)

    //создаем соединение
    let url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chat_id + "&text=" +json
    const formReq = new XMLHttpRequest()
    formReq.open('POST' ,url ,true )
    formReq.setRequestHeader('Content-Type', 'application/json')
	formReq.send(json);
   });
  }(jQuery)
