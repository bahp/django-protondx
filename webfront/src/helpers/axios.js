import qs from 'qs'
import axios from 'axios'

export function post(url, data) {
    return axios.post(apiRoot + url, qs.stringify(data)).then((res) => {
        return res
    })
}

export function get(url, data) {
    return axios.get(apiRoot + url, {params: data})
}
