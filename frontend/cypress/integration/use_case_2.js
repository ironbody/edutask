describe("Requirements 8", () => {
    before(function () {
        // create a fabricated user from a fixture
        cy.fixture('test_user.json')
            .then((user) => {
                cy.request({
                    method: 'POST',
                    url: 'http://localhost:5000/users/create',
                    form: true,
                    body: user
                }).then((response) => {
                    this.uid = response.body._id.$oid

                    // create one fabricated task for that user
                    cy.fixture('test_task.json')
                        .then((task) => {
                            // add the user id to the data of the task object
                            task.userid = this.uid
                            cy.request({
                                method: 'POST',
                                url: 'http://localhost:5000/tasks/create',
                                form: true,
                                body: task
                            }).then((response) => {
                                this.tid = response.body[0]._id.$oid

                                // create new todo
                                cy.fixture('test_todo.json')
                                    .then((todo) => {
                                        // add the task id to the data of the todo object
                                        todo.taskid = this.tid
                                        cy.request({
                                            method: 'POST',
                                            url: 'http://localhost:5000/todos/create',
                                            form: true,
                                            body: todo
                                        })
                                    })
                            })
                        })
                })
            })

        cy.visit("http://localhost:3000/")

        cy.fixture("test_user.json").then((user) => {

            cy.contains("div", "Email Address").find("input").type(user.email)
            cy.get("form").submit()
        })

        cy.contains("Introduction to Bayesian Data Analysis").click()
        
        
    })

    after(function () {
        // clean up by deleting the user from the database
        cy.request({
            method: 'DELETE',
            url: `http://localhost:5000/users/${this.uid}`
        }).then((response) => {
            cy.log(response.body)
        })
    })

    it("Use Case 2.1", function () {
        cy.get('.todo-list > :nth-child(1)').as("item")
        cy.get("@item").find(".checker").click({ force: true })
        cy.get("@item").find(".checker").should("have.class", "checked")
        cy.get("@item").find(".editable").should("have.css", "text-decoration-line", "line-through")
    })
    it("Use Case 2.2", function () {
        cy.get('.todo-list > :nth-child(2)').as("item")
        cy.get('@item').find(".checker").click({ force: true })
        cy.get('@item').find(".checker").should("have.class", "unchecked")
        cy.get('@item').find(".editable").should("have.css", "text-decoration-line", "none")
    })
})