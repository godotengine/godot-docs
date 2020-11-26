"""
    godot_questions_answers
    ~~~~~~~~~~~~~~~~~~~~~~~
    Sphinx extension that adds a ``.. questions-answers:: tag1 tag2 ...`` directive.
    This displays a link to view and ask questions on the Godot Questions & Answers platform.
    This role should be added at the bottom of relevant pages.
    :copyright: Copyright 2020 by The Godot Engine Community
    :license: MIT
"""

from docutils import nodes
from docutils.parsers.rst import Directive, directives

# See <https://github.com/coldfix/sphinx-code-tabs/blob/main/sphinx_code_tabs/__init__.py>
# for setup code inspiration.

# The URL to the questions & answers website.
GODOT_QA_URL = "https://godotengine.org/qa"


class QuestionsAnswersNode(nodes.General, nodes.Element):
    def __init__(self, tags):
        """
        :param str tags: Tags to search for in the Q&A (separated by spaces).
        """
        super(QuestionsAnswersNode, self).__init__()
        self.tags = tags[0]

    @staticmethod
    def visit(spht, node):
        """Append opening tags to document body list."""
        spht.body.append(
            spht.starttag(node, "div", "", **{"class": "questions-answers"})
        )

        spht.body.append(f"""
        <h2>
            Top user questions for “{node.tags}”
            <a href="https://godotengine.org/qa/search?q={node.tags}" target="_blank" rel="noopener" style="font-size: 75%">
                (from Godot Q&amp;A)
            </a>
        </h2>
        """)

        # See `_static/js/godot-questions-answers.js` for the logic.
        spht.body.append(f"""
        <section x-data="questionsAnswers()" x-init="loadQuestions('{node.tags}')">
            <template x-if="questionsLoaded">
                <template x-for="question in questions">
                    <a :href="question.url" target="_blank" rel="noopener">
                        <article class="questions-answers-question">
                            <div class="questions-answers-question-score">
                                <div x-text="question.score" style="font-weight: 700; font-size: 125%"></div>
                                <span x-text="question.score === 1 ? 'vote' : 'votes'">
                            </div>
                            <div class="questions-answers-question-answers" :style="`opacity: ${{question.answers === 0 ? '50%' : '100%'}}`">
                                <div x-text="question.answers" style="font-weight: 700; font-size: 125%"></div>
                                <span x-text="question.answers === 1 ? 'answer' : 'answers'">
                            </div>
                            <div class="questions-answers-question-title" x-text="question.title"></div>
                        </article>
                    </a>
                </template>
            </template>
            <template x-if="!questionsLoaded">
                <p style="text-align: center; height: 40rem; padding-top: 1.5rem; margin-top: 3rem">
                    Loading questions…
                </p>
            </template>
        </section>
        """)

        spht.body.append(
            spht.starttag(
                node,
                "a",
                "Ask a question about “<strong>%s</strong>”" % node.tags,
                href="%s/ask?tags=%s" % (GODOT_QA_URL, node.tags),
                target="_blank",
                rel="noopener",
                title="Ask a question on the Godot Q&A platform (opens in a new tab)",
                **{"class": "questions-answers-btn"},
            )
        )
        spht.body.append("</a>")

    @staticmethod
    def depart(spht, node):
        """Append closing tags to document body list."""
        spht.body.append("</div>")
        # Separate the User questions box from th Previous and Next page buttons.
        spht.body.append("<hr>")


class QuestionsAnswers(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        return [QuestionsAnswersNode(self.content)]


def setup(app):
    app.add_js_file("js/alpine.min.js")
    app.add_js_file("js/godot-questions-answers.js")
    app.add_directive("questions-answers", QuestionsAnswers)
    app.add_node(
        QuestionsAnswersNode,
        html=(QuestionsAnswersNode.visit, QuestionsAnswersNode.depart),
    )

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
