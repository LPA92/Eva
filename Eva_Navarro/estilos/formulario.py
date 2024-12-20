import re
import reflex as rx
import reflex.components.radix.primitives as rdxp


class RadixFormState(rx.State):
    # Estos rastrean la entrada del usuario en tiempo real para su validación.
    user_entered_username: str
    user_entered_email: str

    # Estos son los datos enviados
    username: str
    email: str

    mock_username_db: list[str] = ["reflex", "admin"]

    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(
            r"[^@]+@[^@]+\.[^@]+", self.user_entered_email
        )

    @rx.var
    def username_empty(self) -> bool:
        return not self.user_entered_username.strip()

    @rx.var
    def username_is_taken(self) -> bool:
        return (
            self.user_entered_username
            in self.mock_username_db
        )

    @rx.var
    def input_invalid(self) -> bool:
        return (
            self.invalid_email
            or self.username_is_taken
            or self.username_empty
        )

    def handle_submit(self, form_data: dict):
        """Manejar el envío del formulario."""
        self.username = form_data.get("username")
        self.email = form_data.get("email")


def radix_form_example():
    return rx.flex(
        rx.form.root(
            rx.flex(
                rx.form.field(
                    rx.flex(
                        rx.form.label("Username"),
                        rx.form.control(
                            rx.input(
                                placeholder="Username",
                                # Solución alternativa: parece que se requiere `name` cuando se configura on_change
                                on_change=RadixFormState.set_user_entered_username,
                                name="username",
                            ),
                            as_child=True,
                        ),
                        # El mensaje de validación del lado del servidor se puede mostrar dentro de un rx.cond
                        rx.cond(
                            RadixFormState.username_empty,
                            rx.form.message(
                                "Username cannot be empty",
                                color="var(--red-11)",
                            ),
                        ),
                        # server side validation message can be displayed by `force_match` prop
                        rx.form.message(
                            "Username already taken",
                            # Esta es una solución alternativa:
                            # `force_match` No funciona sin "match"
                            # Este caso no desea validación del lado del cliente
                            # y no se establece intencionalmente "requerido" en la entrada
                            # Entonces "valueMissing" siempre es falso
                            match="valueMissing",
                            force_match=RadixFormState.username_is_taken,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="username",
                    server_invalid=RadixFormState.username_is_taken,
                ),
                rx.form.field(
                    rx.flex(
                        rx.form.label("Email"),
                        rx.form.control(
                            rx.input(
                                placeholder="Email Address",
                                on_change=RadixFormState.set_user_entered_email,
                                name="email",
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "A valid Email is required",
                            match="valueMissing",
                            force_match=RadixFormState.invalid_email,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RadixFormState.invalid_email,
                ),
                rx.form.submit(
                    rx.button(
                        "Submit",
                        disabled=RadixFormState.input_invalid,
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="25em",
            ),
            on_submit=RadixFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(size="4"),
        rx.text(
            "Username submitted: ",
            rx.text(
                RadixFormState.username,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        rx.text(
            "Email submitted: ",
            rx.text(
                RadixFormState.email,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        direction="column",
        spacing="4",
    )