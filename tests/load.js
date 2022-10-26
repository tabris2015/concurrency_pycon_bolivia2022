import http from 'k6/http';
import {check, sleep} from 'k6';
import {FormData} from 'https://jslib.k6.io/formdata/0.0.2/index.js';
import {Trend} from 'k6/metrics';

export const options = {
    // stages: [
    //     { duration: '30s', target: 4},
    //     { duration: '14m', target: 10},
    //     { duration: '10m', target: 10},
    //     { duration: '20m', target: 2},
    //     // { duration: '20s', target: 1},
    // ],
    // discardResponseBodies: true,
    scenarios: {
        contacts: {
            executor: 'shared-iterations',
            vus: 2,
            iterations: 100,
            maxDuration: '1m',
        },
    },
    // scenarios: {
    //     contacts: {
    //       executor: 'constant-arrival-rate',
    //       duration: '25m',
    //       rate: 10,
    //       timeUnit: '1s',
    //       preAllocatedVUs: 20,
    //       maxVUs: 100,
    //     },
    //   },

};

// const config_str = open("config_v1.json")
// const config = JSON.parse(config_str)[__ENV.CONFIG];
// console.log(config)
const imgFile = "street.png"
const binFile = open(imgFile, 'b')


// const inferenceTimeTrend = new Trend('ci_inference_time', true)
// const postTimeTrend = new Trend('ci_postprocess_time', true)
// const serializeTimeTrend = new Trend('ci_serialize_time', true)
// const preTimeTrend = new Trend('ci_preprocess_time', true)
// const totalTimeTrend = new Trend('ci_total_inference_time', true)
// const inputConversionTrend = new Trend('ci_input_conversion_time', true)
// const modelLoadTrend = new Trend('ci_model_loading_time', true)

const httpFile = http.file(binFile, imgFile, 'image/png')
// console.log(config.projectId);
const fd = new FormData();
fd.append('image_file', httpFile);
const body = fd.body();
const url = "http://localhost:8000/predict_od";
const header = {
    'Content-Type': 'multipart/form-data; boundary=' + fd.boundary,
    'accept': 'application/json'
};

export default function () {

    // use this for getting a random modelID from models array
    // const model = config.models[Math.floor(Math.random() * config.models.length)];
    // const path = config.path + `?project_id=${config.projectId}&model_id=${model}` //`/inference/v1/predict?project_id=${project_id}&model_id=${model}`
    // console.log(url)

    const res = http.post(url, body, {headers: header});

    check(res, {'status was 200': (r) => r.status == 200});
    // check(res, {'status was not 429': (r) => r.status != 429});
    // check(res, {'status was not 503': (r) => r.status != 503});
    // check(res, {'status was not 502': (r) => r.status != 502});
    // check(res, {'status was not 499': (r) => r.status != 499});
    console.log(res.status)
    console.log(res.json())
    // if(res.status == 200)
    // {
    //     let data = res.json()['latency']
    //     // console.log(data);
    //     inferenceTimeTrend.add(data['infer_s'] * 1000)
    //     preTimeTrend.add(data['preprocess_s'] * 1000)
    //     postTimeTrend.add(data['postprocess_s'] * 1000)
    //     serializeTimeTrend.add(data['serialize_s'] * 1000)
    //     inputConversionTrend.add(data['input_conversion_s'] * 1000)
    //     modelLoadTrend.add(data['model_loading_s'] * 1000)
    //
    //     totalTimeTrend.add((data['infer_s'] + data['preprocess_s'] + data['postprocess_s'] + data['serialize_s']) * 1000)
    // }


}