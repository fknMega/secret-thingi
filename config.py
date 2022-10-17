config = {
  # F12 -> Console -> Shoutbox.userId
  'user_id': 0,
  # F12 -> Console -> Shoutbox.userToken
  'ws_token': '',

  # Your username
  'username': 'KSZ',



  # Auto Kiss Settings
  "auto_kiss": {
    # Enable auto kiss
    "enabled": True,

    # Auto kiss delay in seconds (random from x to y)
    "delay_from": 1,
    "delay_to": 5,
  },



  # Auto message every x seconds
  "auto_message": {
    # Enable auto message
    "enabled": False,

    # time between messages in seconds
    "time": 2000,

    # messages to send
    "messages": [
      ":wtf:", ':kiss:'
    ],
  },

  # Auto hello response
  "auto_hello": {
    # Enable auto hello response
    "enabled": True,

    # delay in seconds
    "delay": 1,

    # all hellos to respond to
    "hellos": [
      "hello", "hi", "whatsapp", "bonjour", "gm", "morning", 'salut', 'yo', 'hola', ':heyguys:', 'hey', 'howdy'
    ],

    # Responses to send
    "responses": [
      "salut {ping}", "yoo {ping}"
    ]
  },


  # Auto Matket Messages
  "auto_market": {
    # Enable auto market messages
    "enabled": True,

    # delay btw messages in seconds
    "delay": 2000,

    # messages to send
    "messages": [
      "Advertise your products here !!! https://t.me/fknMegaMarket",
    ],
  },




  # Line reader settings
  "line_reader": {
    # Enable line reader
    "enabled": True,

    "command": "/troll",
    

    # Text file to read from
    "file": "lines.txt",

    # Delay between lines in seconds
    "delay": 3
  },


  # Will be added in next update ! ! !

  # Staff detection - Self Destruct
  "staff_detection": {
    # Enable staff detection
    "enabled": True,

    # Time to self destuct for in seconds
    "time": 120,

    # All staff members to detect
    "staff": [ 'KSZ', 'Quessts' ],



}

}
