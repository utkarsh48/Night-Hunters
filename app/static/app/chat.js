const wrapper = document.querySelector('article.wrapper');

class Send{
  constructor(content){
    let messContent = document.createElement("span");
    messContent.classList.add("message-content");
    messContent.innerHTML = content;

    let sendBubble = document.createElement("div");
    sendBubble.classList.add("message-bubble" ,"send0");
    
    sendBubble.appendChild(messContent);
    this.element = sendBubble;
  }
}

class Recieve{
  constructor(content){
    let messContent = document.createElement("span");
    messContent.classList.add("message-content");
    messContent.innerHTML = content;

    let recieveBubble = document.createElement("div");
    recieveBubble.classList.add("message-bubble" ,"recieve0");
    
    recieveBubble.appendChild(messContent);
    this.element = recieveBubble;
  }
}