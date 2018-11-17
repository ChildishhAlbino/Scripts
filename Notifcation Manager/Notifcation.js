

class NotificationManager{

    subscribers;

    constructor(subscribers = Subscriber){
        print("Made")
    }

    notify(){
        forea
    }

    addSubscriber(){

    }
    
}

class Subscriber{

    pushNotification(notification = Notification){
        console.log(notification.text)
    }

}

class Notification{ 
    text;
    
    constructor(text){
        this.text = text;
    }
}

module.exports = NotificationManager

