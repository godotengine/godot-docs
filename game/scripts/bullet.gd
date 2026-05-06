extends Area2D

# Docs ref: tutorials/scripting/instancing_with_signals.rst - bullet pattern
# Docs ref: tutorials/physics/using_area_2d.rst - body_entered / area_entered signals

const SPEED = 600.0
const ROOM_BOUNDS = Rect2(0, 0, 800, 600)

var velocity: Vector2 = Vector2.ZERO

func setup(direction: Vector2) -> void:
	velocity = direction * SPEED
	rotation = direction.angle()

func _ready() -> void:
	body_entered.connect(_on_body_entered)
	area_entered.connect(_on_area_entered)

func _physics_process(delta: float) -> void:
	position += velocity * delta
	if not ROOM_BOUNDS.has_point(position):
		queue_free()

func _on_body_entered(_body: Node2D) -> void:
	queue_free()

func _on_area_entered(area: Area2D) -> void:
	if area.is_in_group("enemies"):
		area.queue_free()
	queue_free()
