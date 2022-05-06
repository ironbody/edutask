describe("Requirements 8", () => {
    before(() => {
        cy.visit("http://localhost:3000/")
        cy.fixture("test_user.json").then((user) => {

            cy.contains("a", "Have no account yet? Click here to sign up.").click()
            cy.contains("div", "Email Address").find("input").type(user.email)
            cy.contains("div", "First Name").find("input").type(user.firstName)
            cy.contains("div", "Last Name").find("input").type(user.lastName)
            cy.get("form").submit()

            cy.contains("div", "Title").find("input").type(user.tasks[0].title)
            cy.contains("div", "YouTube URL").find("input").type(user.tasks[0].url)
            cy.get("form").submit()
        })

        cy.get(".container").contains("div", "Improve Devtools").click()
    })

    after(function () {
        cy.fixture("test_user.json").then((user) => {
            cy.request("GET", "http://localhost:5000/users/bymail/" + user.email)
                .then((res) => {
                    const userId = res.body._id.$oid
                    cy.request("DELETE", "http://localhost:5000/users/" + userId)
                })

        })

    })

    it("Use Case 2.1", () => {
        cy.get('.todo-list > :nth-child(1)').find(".checker").click({ force: true })
        cy.get('.todo-list > :nth-child(1)').find(".editable").should("have.css", "text-decoration-line", "line-through")
    })
})