extends Node2D

# Docs ref: tutorials/scripting/instancing_with_signals.rst - spawning bullets via signal
# Docs ref: tutorials/physics/physics_introduction.rst - StaticBody2D for walls

const ROOM_W = 800
const ROOM_H = 600
const WALL_T = 20

@onready var player: CharacterBody2D = $Player

var _bullet_scene: PackedScene = preload("res://scenes/bullet.tscn")
var _enemy_scene: PackedScene = preload("res://scenes/enemy.tscn")

func _ready() -> void:
	player.shoot.connect(_on_player_shoot)
	_create_walls()
	_spawn_enemies()

func _on_player_shoot(direction: Vector2, from_pos: Vector2) -> void:
	var bullet = _bullet_scene.instantiate()
	add_child(bullet)
	bullet.global_position = from_pos
	bullet.setup(direction)

func _create_walls() -> void:
	# top, bottom, left, right
	_make_wall(ROOM_W / 2.0, WALL_T / 2.0,          ROOM_W,  WALL_T)
	_make_wall(ROOM_W / 2.0, ROOM_H - WALL_T / 2.0, ROOM_W,  WALL_T)
	_make_wall(WALL_T / 2.0, ROOM_H / 2.0,          WALL_T,  ROOM_H)
	_make_wall(ROOM_W - WALL_T / 2.0, ROOM_H / 2.0, WALL_T,  ROOM_H)

func _make_wall(cx: float, cy: float, w: float, h: float) -> void:
	var wall := StaticBody2D.new()
	add_child(wall)
	wall.global_position = Vector2(cx, cy)

	var col := CollisionShape2D.new()
	var shape := RectangleShape2D.new()
	shape.size = Vector2(w, h)
	col.shape = shape
	wall.add_child(col)

	var vis := Polygon2D.new()
	var hw := w / 2.0
	var hh := h / 2.0
	vis.polygon = PackedVector2Array([
		Vector2(-hw, -hh), Vector2(hw, -hh),
		Vector2(hw,  hh),  Vector2(-hw, hh)
	])
	vis.color = Color(0.45, 0.45, 0.45)
	wall.add_child(vis)

func _spawn_enemies() -> void:
	var positions := [
		Vector2(200, 150), Vector2(400, 150), Vector2(600, 150),
		Vector2(150, 350), Vector2(650, 350),
		Vector2(300, 450), Vector2(500, 450),
	]
	for pos in positions:
		var enemy = _enemy_scene.instantiate()
		add_child(enemy)
		enemy.global_position = pos
