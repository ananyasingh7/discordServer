const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
    console.log('ready');
});

client.on('message',(message) => {
    console.log(message.content);
    console.log(message.member.displayName);
})



client.login('NzEzNTYyMjQxMDcyNDk2NzMx.Xsh6nw.ZM1WAl3_pvfbovzV6KxEyFeMB08');