.. _doc_gui_elements_reference_table:

============================================
Cross-Framework UI Component Mapping
============================================

This table maps common UI components, containers, layout systems, event mechanisms, and styling paradigms
across iOS (UIKit & SwiftUI), Android (Android Views & Jetpack Compose), and Godot Engine (Control Nodes).

.. list-table:: UI Component Comparison Matrix
   :widths: 15 20 18 18 18 18 18 25
   :header-rows: 1

   * - Category
     - Feature / UI Element
     - Godot Control Node
     - iOS UIKit (Swift)
     - iOS SwiftUI
     - Android View (XML / Code)
     - Kotlin Jetpack Compose
     - Primary Function
   * - Base Views
     - Base Container / Screen
     - ``Control``
     - ``UIView``
     - ``View`` / ``ZStack``
     - ``View``
     - ``Box`` / ``Modifier``
     - Base visual container with spatial bounds.
   * - Text & Display
     - Static Text
     - ``Label`` / ``RichTextLabel``
     - ``UILabel``
     - ``Text()``
     - ``TextView``
     - ``Text()``
     - Displays static or formatted text.
   * - Text Input
     - Single-line Input
     - ``LineEdit``
     - ``UITextField``
     - ``TextField()``
     - ``EditText``
     - ``TextField()``
     - Single-line user text input field.
   * - Text Input
     - Multi-line Input
     - ``TextEdit``
     - ``UITextView``
     - ``TextEditor()``
     - ``EditText`` (multiline)
     - ``TextField(singleLine = false)``
     - Multi-line editable text region.
   * - Controls & Inputs
     - Standard Button
     - ``Button``
     - ``UIButton``
     - ``Button()``
     - ``Button``
     - ``Button()``
     - Push button with label or icon.
   * - Controls & Inputs
     - Image Button
     - ``TextureButton``
     - ``UIButton`` (with image)
     - ``Button { Image() }``
     - ``ImageButton``
     - ``IconButton()``
     - Button rendered using custom textures or sprites.
   * - Controls & Inputs
     - Image Display
     - ``TextureRect``
     - ``UIImageView``
     - ``Image()`` / ``AsyncImage()``
     - ``ImageView``
     - ``Image()`` / ``AsyncImage()``
     - Renders 2D textures, bitmaps, or images.
   * - Controls & Inputs
     - Toggle Switch
     - ``CheckButton``
     - ``UISwitch``
     - ``Toggle()``
     - ``Switch``
     - ``Switch()``
     - Binary state toggle control.
   * - Controls & Inputs
     - Checkbox
     - ``CheckBox``
     - ``UIButton`` (custom)
     - ``Toggle().toggleStyle(.checkbox)``
     - ``CheckBox``
     - ``Checkbox()``
     - Standard checkbox toggle input.
   * - Controls & Inputs
     - Dropdown / Selection
     - ``OptionButton``
     - ``UIPickerView`` / ``Menu``
     - ``Picker()`` / ``Menu()``
     - ``Spinner``
     - ``DropdownMenu()``
     - Selectable dropdown option list.
   * - Controls & Inputs
     - Range Slider
     - ``HSlider`` / ``VSlider``
     - ``UISlider``
     - ``Slider()``
     - ``SeekBar``
     - ``Slider()``
     - Continuous or discrete value slider.
   * - Controls & Inputs
     - Number Stepper
     - ``SpinBox``
     - ``UIStepper``
     - ``Stepper()``
     - ``NumberPicker``
     - ``Stepper()``
     - Numeric input with step increment arrows.
   * - Controls & Inputs
     - Progress Bar
     - ``ProgressBar``
     - ``UIProgressView``
     - ``ProgressView()``
     - ``ProgressBar``
     - ``LinearProgressIndicator()``
     - Visual progress fill indicator.
   * - Layout & Containers
     - Vertical Stack
     - ``VBoxContainer``
     - ``UIStackView`` (vertical)
     - ``VStack``
     - ``LinearLayout`` (vertical)
     - ``Column()``
     - Automatically stacks children vertically.
   * - Layout & Containers
     - Horizontal Stack
     - ``HBoxContainer``
     - ``UIStackView`` (horizontal)
     - ``HStack``
     - ``LinearLayout`` (horizontal)
     - ``Row()``
     - Automatically stacks children horizontally.
   * - Layout & Containers
     - Card / Panel Container
     - ``PanelContainer``
     - ``UIView`` (layer background)
     - ``ZStack`` / background
     - ``CardView``
     - ``Card()``
     - Group container styled with background box.
   * - Layout & Containers
     - Scrollable Area
     - ``ScrollContainer``
     - ``UIScrollView``
     - ``ScrollView``
     - ``ScrollView``
     - ``Modifier.verticalScroll()``
     - Scrollable viewport for overflow content.
   * - Lists & Grids
     - Scrollable List
     - ``ItemList`` / ``VBox`` + Scroll
     - ``UITableView``
     - ``List`` / ``LazyVStack``
     - ``RecyclerView``
     - ``LazyColumn()``
     - Dynamic vertical listing of rows.
   * - Lists & Grids
     - Grid View
     - ``GridContainer``
     - ``UICollectionView``
     - ``LazyVGrid``
     - ``RecyclerView`` (GridLayout)
     - ``LazyVerticalGrid()``
     - Multi-column row and grid layout.
   * - Mechanics
     - Layout Engine
     - Containers & Anchors
     - Auto Layout / Constraints
     - Layout modifiers / Frames
     - ``ConstraintLayout``
     - Layout Modifiers
     - Controls spatial sizing and responsive placement.
   * - Mechanics
     - Click / Event Handling
     - Signal (``pressed.connect()``)
     - ``addTarget()`` / ``UIAction``
     - Button action / ``onTapGesture``
     - ``setOnClickListener()``
     - ``onClick = { }``
     - Binds user interaction to executable code.
   * - Mechanics
     - Styling System
     - Theme Engine & ``StyleBox``
     - Programmatic / ``UIAppearance``
     - ``ViewModifiers``
     - XML Styles & Themes
     - ``MaterialTheme``
     - Applies themes, colors, and layout borders.
