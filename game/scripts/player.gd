extends CharacterBody2D

# Docs ref: tutorials/2d/2d_movement.rst - 8-way movement pattern
# Docs ref: tutorials/inputs/input_examples.rst - event vs polling input

const SPEED = 300.0

signal shoot(direction: Vector2, from_position: Vector2)

func _physics_process(_delta: float) -> void:
	var input_dir = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = input_dir * SPEED
	move_and_slide()

func _input(event: InputEvent) -> void:
	if event.is_action_pressed("shoot"):
		var mouse_pos = get_global_mouse_position()
		var direction = (mouse_pos - global_position).normalized()
		shoot.emit(direction, global_position)
