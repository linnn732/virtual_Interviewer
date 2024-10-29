let userWebcam = document.getElementById('userWebcam');
let videoArea = document.getElementById('video');
let black = document.getElementById('black');
let recordedVideo = document.getElementById('recordedVideo');

let startCamera = document.getElementById('startBtn'); 
let recordBtn = document.getElementById('recordBtn');
let playBtn = document.getElementById('playBtn');
let submitBtn = document.getElementById('submitBtn');
let playRecorded = document.getElementById('playRecorded');



let mediaRecorder;
let recordedBlobs;

recordBtn.addEventListener('click', () => {

    if (recordBtn.textContent === '開始錄製') {

        startRecording();

    } else {

        stopRecording();
        recordBtn.textContent = '開始錄製';
        playRecorded.disabled = false;
        
    }
});

playBtn.addEventListener('click', () => {

    if (playBtn.textContent === "播放影片") {

        videoArea.play();
        playBtn.textContent = "暫停"

    } else {

        videoArea.pause();
        playBtn.textContent = '播放影片';
        
    }
    
});

playRecorded.addEventListener('click', () => {

    if (playRecorded.textContent === "播放錄製影片") {

        const superBuffer = new Blob(recordedBlobs, { type: 'video/webm' });
        recordedVideo.src = null;
        recordedVideo.srcObject = null;
        recordedVideo.src = window.URL.createObjectURL(superBuffer);
        recordedVideo.controls = true;
        recordedVideo.play();
        
        playRecorded.textContent = "暫停播放影片"

    } else {

        recordedVideo.pause();
        playRecorded.textContent = '播放錄製影片';


    }
    
})

submitBtn.addEventListener('click', () => {
    alert("已提交");
    return false;
})



function handleDataAvailable(event) {

    console.log('handleDataAvailable', event);
    if (event.data && event.data.size > 0) {
        recordedBlobs.push(event.data);
    }

}


function startRecording() {

    recordedBlobs = [];
    let options = { mimeType: 'video/webm;codecs=vp9,opus' };

    if (!MediaRecorder.isTypeSupported(options.mimeType)) {

        console.error(`${options.mimeType} is not supported`);
        options = { mimeType: 'video/webm;codecs=vp8,opus' };

        if (!MediaRecorder.isTypeSupported(options.mimeType)) {

            console.error(`${options.mimeType} is not supported`);
            options = { mimeType: 'video/webm' };

            if (!MediaRecorder.isTypeSupported(options.mimeType)) {

                console.error(`${options.mimeType} is not supported`);
                options = { mimeType: '' };

            }

        }

    }

    try {
        mediaRecorder = new MediaRecorder(window.stream, options);
    } catch (e) {
        console.error('Exception while creating MediaRecorder:', e);
        // errorMsgElement.innerHTML = `Exception while creating MediaRecorder: ${JSON.stringify(e)}`;
        // return;
    }

    console.log('Created MediaRecorder', mediaRecorder, 'with options', options);
    recordBtn.textContent = "停止錄製";
    playRecorded.disabled = true;

    mediaRecorder.onstop = (event) => {
        console.log('Recorder stopped: ', event);
        console.log('Recorded Blobs: ', recordedBlobs);
    };

    mediaRecorder.ondataavailable = handleDataAvailable;
    mediaRecorder.start();
    console.log('MediaRecorder started', mediaRecorder);
}

//停止錄製
function stopRecording() {
    mediaRecorder.stop();
}


function handleSuccess(stream) {
    // recordButton.disabled = false;
    console.log('getUserMedia() got stream:', stream);
    window.stream = stream;

    userWebcam.srcObject = stream;
}

async function init(constraints) {
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    } catch (e) {
        console.error('navigator.getUserMedia error:', e);
        // errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
    }
}

startCamera.addEventListener('click', async () => {
   
    const constraints = {
        audio: {
            echoCancellation: { exact: true }
        },
        video: {
            width: 1280, height: 720
        }
    };
    console.log('Using media constraints:', constraints);
    await init(constraints);

       
})


