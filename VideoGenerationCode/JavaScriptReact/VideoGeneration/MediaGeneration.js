const getVideosAndDurations = require('../Models/PexelsVideo');

const getPexelsVideos = async (query, targetDuration) => {
    const allUrls = await getVideosAndDurations(query, 30 , 16 / 9, 0.6);

    allUrls.sort((a, b) => a.duration - b.duration);

    let selectedVideos = [];
    let currentDuration = 0;

    for (let video of allUrls) {
        if (currentDuration + video.duration <= targetDuration) {
            selectedVideos.push(video.videoUrl);
            currentDuration += video.duration;
        } else {
            break;
        }
    }

    return selectedVideos;
};



export default getPexelsVideos;