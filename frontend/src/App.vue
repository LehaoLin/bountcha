<template>
  <div class="video">
    <center style="margin-top: 30vh">
      <p>
        Please play the video and check the boundary. You can seek by move the
        slider and also use "Space" keyboard to play/pause.
      </p>
      <video
        width="400"
        id="video1"
        class="video1"
        :src="video_src"
        ref="video1"
        muted
      ></video>
      <div>
        <el-button @click="play" style="width: 400px" v-if="!play_status"
          >Play</el-button
        >
        <el-button @click="play" style="width: 400px" v-if="play_status"
          >Pause</el-button
        >
      </div>
      <div style="width: 400px; font-size: 15px">
        {{ round(slider / 1000) }}/{{ duration / 1000 }}
      </div>
      <el-slider
        v-model="slider"
        :max="duration"
        :min="0"
        style="width: 400px"
        @input="slider_input"
        :show-tooltip="false"
      ></el-slider>

      <div>
        <el-button style="width: 400px" @click="verify">Submit</el-button>
      </div>
    </center>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { onKeyStroke } from "@vueuse/core";
import { ElLoading } from "element-plus";

const video1 = ref(null);
const status = ref(0);

import { ElNotification } from "element-plus";
const user_id = ref("");

const video_src = ref("");

const slider = ref(0);

const slider_input = () => {
  if (play_status.value) {
    play_status.value = false;
    video1.value.pause();
    clearInterval(intervalId.value);
  }
  video1.value.currentTime = slider.value / 1000;
};

const round = (number) => {
  return number.toFixed(3);
};

onMounted(async () => {
  await enter_video("test.mp4");
  onKeyStroke(" ", (e) => {
    console.log("space");
    if (status.value === 2) {
      play();
    }
  });
});

const intervalId = ref("");

const duration = ref(0);

const play_status = ref(false);
const play = () => {
  if (play_status.value) {
    video1.value.pause();
    clearInterval(intervalId.value);
    play_status.value = false;
  } else {
    video1.value.play();
    const set_time = () => {
      slider.value = video1.value.currentTime * 1000;
    };
    video1.value.onplay = () => {
      intervalId.value = setInterval(set_time, 100);
    };
    play_status.value = true;
  }
};

const downFile = async (src) => {
  let r = await axios({
    url: src,
    method: "GET",
    responseType: "blob",
  });
  const href = URL.createObjectURL(r.data);
  video_src.value = href;
};

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const video_name = ref("");
const loading = ref();

const enter_video = async (name) => {
  loading.value = ElLoading.service({ fullscreen: true });
  status.value = 2;
  video_name.value = name;
  let url = `/video/${name}`;
  await downFile(url);
  await sleep(500);
  duration.value = video1.value.duration * 1000;
  loading.value.close();
};

const verify = async () => {
  let res = await axios({
    method: "post",
    url: "verify",
    data: {
      id: user_id.value,
      name: video_name.value,
      currentTime: video1.value.currentTime,
    },
  });
  if (res.data.msg === 1) {
    ElNotification({
      title: "You pass the CAPTCHA",
      type: "success",
    });
  } else {
    ElNotification({
      title: "You don't pass the CAPTCHA",
      type: "error",
    });
  }
};
</script>

<style scoped>
.login {
  margin-top: 50vh;
}
.video1 {
  z-index: 1 !important;
}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
