import axios from "axios";

export const handleTaskGet = async (getter, id) => {
  await axios.get(`http://localhost:5000/api/task/${id}`).then(e => getter(e.data));
}

export const handleTaskCheck = async (ans, id, getter) => {
  await axios.post(`http://localhost:5000/api/check/${id}`, ans).then(e => getter(e.data));
}