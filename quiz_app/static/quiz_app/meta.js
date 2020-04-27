// extracts data from html
async function answerSelected(e) {
    // e.classList.remove("btn-primary");
        const answer_id = e.id.split('_')[1];
        const question_id = e.parentNode.parentNode.id.split('_')[1];

      const data = {
        "question_id": parseInt(question_id),
        "answer_id": parseInt(answer_id)
      };
      const response = await postApi(data);
      if (response['answer_id'] === data['answer_id']) {
          e.classList.add("btn-success");
      }
      else {
          e.classList.add("btn-danger");
          const correct_answer = document.getElementById(`answer_${response['answer_id']}`);
          correct_answer.classList.add("btn-success");
      }
}

// sends data to server and returns response
async function postApi(data) {
    const csrf = document.getElementById('csrf').textContent;
    const options = {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrf
    }
  };

    try {
        const res = await fetch(`/check/`, options);
        if (!res.ok) {
            throw new Error(res.status);
        }
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}