from playwright.sync_api import Page, expect


class TestMainPage:
    def test_user_can_see_title(self, page: Page):
        locator = page.locator(".stMarkdown h1")
        title = "Welcome to UrFU ML Engineering 2022, Group 20 project"
        expect(locator).to_have_text(title, timeout=10000)

    def test_user_can_see_authors(self, page: Page):
        authors_title_locator = page.locator(".element-container h3")
        authors_title_text = "Authors:"
        expect(authors_title_locator).to_have_text(authors_title_text)
        expect(page.get_by_role("listitem")).to_have_count(4)
        expect(page.get_by_role("listitem")).to_have_text(
            [
                "Vladimir Katin katin.v.v.@gmail.com",
                "Anton Bessolitsyn Anton.Bessolitsyn@hotmail.com",
                "Alexander Orlov eaglophone@gmail.com",
                "Anna Bezhenar asbezhenar@gmail.com",
            ]
        )

    def test_user_can_see_input_field(self, page: Page):
        input_field = page.locator(".stTextInput input")
        expect(input_field).to_be_editable()

    def test_user_can_see_github_link(self, page: Page):
        git_hub_url_locator = page.locator(".element-container p a")
        expect(git_hub_url_locator).to_have_attribute(
            "href", "https://github.com/urfuMagDS2022SFgroup/sf_data_science_python"
        )
