// Don't end the URL below with a trailing slash.
const QA_API_URL = "http://devd.io:8001";

/**
 * Returns an object for use by Alpine.js.
 * See `godot_questions_answers.py`.
 */
function questionsAnswers() {
  return {
    questions: [],
    questionsLoaded: false,

    loadQuestions(tag) {
      $.getJSON(`${QA_API_URL}/${tag}.json`, {}).then((response) => {
        this.questions = response.data.questions;
        this.questionsLoaded = true;
      });
    }
  };
}
